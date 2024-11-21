#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Hyperspectral Imaging dataset manager.

    AUTHOR
    ------------------------------------------------------------------------
    Name:       Alberto Martín Pérez
    Contact:    a.martinp@upm.es

    SUMMARY
    ------------------------------------------------------------------------
    This file contains classes to manage ground-truth maps labeled by
    neurosurgeons during the Hyperspectral project.
   """

from dataclasses import dataclass
from typing import Any, Dict, Tuple, Union, List

import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from scipy.io import loadmat

from hsi_labels import HSI_LABEL_INFO
from helpers import check_path


@dataclass
class GroundTruthDataResults:
    """
    Dataclass that stores all the variables in the `dataResults` structure
    stored inside a `.mat` ground-truth file.
    """

    number_of_reference_pixels: int
    reference_spectrum: NDArray[np.double]
    reference_pixel_coord: NDArray
    reference_class: Tuple[str]
    threshhold_value: NDArray
    comment: Tuple[str]
    gt_map: NDArray
    rgb_image: NDArray[np.uint8]
    rgb_reference: NDArray[np.uint8]
    color_gt_map_r: NDArray[np.double]
    color_gt_map_g: NDArray[np.double]
    color_gt_map_b: NDArray[np.double]
    axs_rgb: NDArray
    gt: NDArray[np.double]


class GroundTruthMap:
    """
    GroundTruthMap to manage `*gtID*_cropped_Pre-processed` files.
    This class should not be used by the user.
    """

    def __init__(self, path: str, patient_id: Union[str, List[str]]) -> None:
        """
        GroundTruthMap class constructor to load `*gtID*_cropped_Pre-processed.mat` files.
        Once the instance has been created, it automatically loads the preprocessed image.

        Parameters
        ----------
        - `path`:             Path from where to load the preprocessed image.
        - `patients`:         Patient ID to be loaded
        """

        self.path = path

        if not isinstance(patient_id, str):
            print(
                f"{type(self).__name__} can only load 1 string object at a time. {type(patient_id)} object was passed instead."
            )
            raise AttributeError(
                f"{type(self).__name__} can only load 1 string object at a time. {type(patient_id)} object was passed instead."
            )
        else:
            self._patient_id = patient_id

        # File attributes
        self.__header__: str = ""
        self.__version__: str = ""
        self.__globals__ = None
        self._groundTruthMap: NDArray[Any] = np.array(None)
        self._dataResults: GroundTruthDataResults = None

        self._colored_gt: NDArray[Any] = np.array(None)

        # Automatically load the patients ground truth image
        self.load()
        self.compute_map()

    @property
    def patient_id(self) -> str:
        """Retrieve the patient id of the loaded ground-truth map."""
        return self._patient_id

    @property
    def header(self) -> str:
        """Header used when storing the ground-truth map with Matlab."""
        return self.__header__

    @property
    def version(self) -> str:
        """Version used when storing the ground-truth map with Matlab."""
        return self.__version__

    @property
    def globals(self):
        """Global variables used when storing the ground-truth map with Matlab."""
        return self.__globals__

    @property
    def groundTruthMap(self) -> NDArray[Any]:
        """
        `groundTruthMap` property of the loaded preprocessed image.
        It returns `None` if the *gtID*_cropped_Pre-processed.mat` file
        has not been loaded.
        """
        return self._groundTruthMap

    @property
    def dataResults(self) -> GroundTruthDataResults:
        """
        `dataResults` property of the loaded preprocessed image.
        It returns `None` if the *gtID*_cropped_Pre-processed.mat` file
        has not been loaded.
        """
        return self._dataResults

    def plot(
        self,
        title: str,
        show_axis: bool = False,
        path_: str = "./",
        file_suffix: str = "suffix",
        file_format: str = "png",
    ) -> None:
        """
        Save the computed classification map. It does nothing if the map has not been computed.
        Additionally, it can also show the plot

        Parameters
        ----------
        - `title`:          Title of the plot.
        - `show_axis`:      Flag to show the coordenates in all axis of the plot
        - `path_`:          Path to save the bar plot in disk memory.
        - `file_suffix`:    String to use as suffix to differentiate saved files.
        - `file_format`:    File extension when saving the figure. (E.g. '.png', '.svg').
            - Supported formats: `eps`, `jpeg`, `jpg`, `pdf`, `pgf`, `png`, `ps`, `raw`, `rgba`, `svg`, `svgz`, `tif`, `tiff`.
        """

        fig = plt.figure()
        plt.title(title)
        plt.imshow(self._colored_gt)

        # Use this to stop showing coordenate axis for the GT map
        if not show_axis:
            plt.axis("off")

        plt.tight_layout()  # Resize layout so nothing is cropped in the image

        # Save plot in specific format to disk memory if specified by user. Otherwise, just show
        path_ = check_path(path_)
        save_path = f"{path_}GroundTruthMap_{file_suffix}.{file_format}"
        plt.savefig(save_path, bbox_inches="tight")
        plt.close()

    def load(self) -> None:
        """
        Loads the patient ground-truth map using the ID passed to the class constructor.
        """
        mat_file = self.load_patient_gt(file_path=self.path, patient_id=self._patient_id)

        self.__header__ = mat_file["__header__"]
        self.__version__ = mat_file["__version__"]
        self.__globals__ = mat_file["__globals__"]

        try:
            self._groundTruthMap = mat_file["groundTruthMap"].astype(np.int16)
        except KeyError:
            self._groundTruthMap = None

        data_results: NDArray = mat_file["dataResults"]

        try:
            rgb_reference = data_results["rgbReference"][0, 0]
        except ValueError:
            rgb_reference = None

        try:
            axs_rgb = data_results["axsRgb"][0, 0]
        except ValueError:
            axs_rgb = None

        self._dataResults = GroundTruthDataResults(
            number_of_reference_pixels=data_results["numberOfReferencePixels"][0, 0][0, 0],
            reference_spectrum=data_results["referenceSpectrum"][0, 0],
            reference_pixel_coord=data_results["referencePixelCoord"][0, 0],
            reference_class=data_results["referenceClass"][0, 0],
            threshhold_value=data_results["thresholdValue"][0, 0],
            comment=data_results["comment"][0, 0],
            gt_map=data_results["GTmap"][0, 0],
            rgb_image=data_results["rgbImage"][0, 0],
            rgb_reference=rgb_reference,
            color_gt_map_r=data_results["colorGTMapR"][0, 0],
            color_gt_map_g=data_results["colorGTMapG"][0, 0],
            color_gt_map_b=data_results["colorGTMapB"][0, 0],
            axs_rgb=axs_rgb,
            gt=data_results["GT"][0, 0],
        )

        print(f"The ground truth image from patient {self._patient_id} has been loaded.")

    def load_patient_gt(self, file_path: str, patient_id: str) -> Dict[str, Any]:
        """
        Loads a single patient preprocessed image.

        Parameters
        ----------
        - `file_path`: Path with the file to be loaded.
        - `patient_id`: ID of the patient ground-truth to load.

        Returns
        -------
        - Python dictionary with the following properties:
            - `patient_id`
            - `__header__`
            - `__version__`
            - `__globals__`
            - `groundTruthMap`
            - `dataResults`
        """
        print(f"Loading patient {patient_id} at {file_path}...")

        if not file_path.endswith("/"):
            file_path = f"{file_path}/"

        return loadmat(f"{file_path}SNAPgt{patient_id}_cropped_Pre-processed.mat")

    def compute_map(self) -> None:
        """
        Generates a color map by translating each label value to an RGB value.
        """

        # Get all label references
        label_refs: NDArray[Any] = np.array(list(HSI_LABEL_INFO.keys()))

        # Get all label color references
        label_colors: NDArray[Any] = np.array(
            [HSI_LABEL_INFO[label]["Color"] for label in label_refs]
        )

        image_rgb: NDArray[Any] = np.zeros(
            (self._groundTruthMap.shape[0], self._groundTruthMap.shape[1], 3),
            dtype=np.uint8,
        )

        # For every label in the input map, add the appropiate color
        for label in np.unique(self._groundTruthMap):
            x, y = np.where(self._groundTruthMap == label)  # Get pixel coordinates
            colour_ref = np.where(label_refs == str(label))  # Get color reference
            image_rgb[x, y, :] = label_colors[colour_ref]  # Add color to all pixels

        self._colored_gt = image_rgb
