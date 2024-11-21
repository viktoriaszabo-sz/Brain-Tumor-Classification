import os
from scipy.io import loadmat
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from classification_maps import ClassificationMap  # Ensure these modules exist
from ground_truth_maps import GroundTruthMap  # Ensure these modules exist

# Load the .mat file to a variable
patient_1_dataset = loadmat(r"Brain_SVM//data/dataset/ID0065C01_dataset.mat")

# Understand what loadmat returns
print(type(patient_1_dataset))

# See what elements are contained in the dataset
print(patient_1_dataset.keys())

# Extract data and labels
data = patient_1_dataset['data']
labels = patient_1_dataset['label']
print(f"'data' type: {type(data)}")
print(f"'labels' type: {type(labels)}")
print(f"Samples array size: {data.shape}")
print(f"Labels array size: {labels.shape}")

# Seed for reproducibility
seed = 2022

# ------------------------------------------------------
# Load datasets from other patients and combine them
patient_2_dataset = loadmat(r"Brain_SVM/data/dataset/ID0067C01_dataset.mat")
patient_3_dataset = loadmat(r"Brain_SVM/data/dataset/ID0070C02_dataset.mat")

data = np.concatenate(
    [
        patient_1_dataset["data"],
        patient_2_dataset["data"],
        patient_3_dataset["data"],
    ],
    axis=0,
)
labels = np.concatenate(
    [
        patient_1_dataset["label"],
        patient_2_dataset["label"],
        patient_3_dataset["label"],
    ],
    axis=0,
)
# See the dimensions of "data" and "labels"
print(f"Samples array size: {data.shape}")
print(f"Labels array size: {labels.shape}")

# Check unique labels
print(f"Unique labels: {np.unique(labels, return_counts=True)}")
print(f"Different number of labels: {len(np.unique(labels))}")

# Reshape labels for model training
labels = labels.ravel()
print(f"New shape of labels array: {labels.shape}")

# ------------------------------------------------------
# Create an instance of the model and train
model = SVC(kernel="linear", probability=True, random_state=seed)
model.fit(X=data, y=labels)

# Compute the accuracy of predictions
predictions = model.predict(X=data)
acc = accuracy_score(y_true=labels, y_pred=predictions)
print(f"ACCURACY: {100*acc:.2f}%")

# Load and reshape hyperspectral cube
patient_id = "ID0071C02"
preprocessed_mat = loadmat(rf"Brain_SVM/data/cubes/SNAPimages{patient_id}_cropped_Pre-processed.mat")
cube = preprocessed_mat["preProcessedImage"]

# Reshape cube for prediction
assert len(cube.shape) == 3, "Cube must have 3 dimensions (width, height, bands)."
cube_reshaped = cube.reshape((cube.shape[0] * cube.shape[1]), cube.shape[2])
pred_map = model.predict_proba(X=cube_reshaped)

# Generate and save classification map
os.makedirs("./outputs/", exist_ok=True)
cls_map = ClassificationMap(
    map=pred_map,
    cube_shape=cube.shape,
    unique_labels=np.unique(labels),
)
cls_map.plot(
    title=f"Patient classified with {type(model).__name__}",
    show_axis=False,
    path_="./outputs/",
    file_suffix=f"{patient_id}",
    file_format="png",
)

# Generate ground truth map
gt = GroundTruthMap(r"Brain_SVM/data/ground-truth/", patient_id)
gt.plot(
    title=f"Ground truth from patient {patient_id}",
    show_axis=False,
    path_="./outputs/",
    file_suffix=f"GT_{patient_id}",
    file_format="png",
)

# ------------------------------------------------------
# Hyperparameter optimization with GridSearchCV
hyperparameters = {"kernel": ("linear", "rbf"), "C": [1], "gamma": [1]}
model = GridSearchCV(
    estimator=SVC(probability=True, random_state=seed),
    param_grid=hyperparameters,
    verbose=4,
    cv=5,  # Cross-validation folds
)
model.fit(X=data, y=labels)
print(f"Best parameters found: {model.best_params_}")

# Predict data from a new patient dataset
patient_new_dataset = loadmat(r"Brain_SVM/data/dataset/ID0071C02_dataset")  # Example file
new_predictions = model.predict(patient_new_dataset["data"])
new_acc = accuracy_score(y_true=patient_new_dataset["label"].ravel(), y_pred=new_predictions)
print(f"ACCURACY (on new data with optimized SVM): {100*new_acc:.2f}%")

# Classify image with optimized SVM
pred_map = model.predict_proba(X=cube_reshaped)
cls_map = ClassificationMap(
    map=pred_map,
    cube_shape=cube.shape,
    unique_labels=np.unique(labels),
)
cls_map.plot(
    title=f"Patient classified with optimized {type(model.estimator).__name__}",
    show_axis=False,
    path_="./outputs/",
    file_suffix=f"{patient_id}_optimized",
    file_format="png",
)
