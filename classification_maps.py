#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Hyperspectral classification metrics and maps manager.

    AUTHOR
    ------------------------------------------------------------------------
    Name:       Alberto Martín Pérez
    Contact:    a.martinp@upm.es

    SUMMARY
    ------------------------------------------------------------------------
    This file contains classes to compute classification metrics and
    classification maps after predicting data.
   """

from typing import Any, List, Union


import numpy as np
from numpy.typing import NDArray
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from hsi_labels import HSI_LABEL_INFO
from helpers import check_path


class ClassificationMap:
    """Class to compute binary and probabilistic classification maps."""

    def __init__(
        self, cube_shape: NDArray[Any], map: NDArray[Any], unique_labels: NDArray[Any]
    ) -> None:
        """

        Parameters
        ----------
        - `cube_shape`: Shape of the classified cube.
        - `map`: Numpy vector of shape (n_samples, n_clases) with predicted label
        probabilities by a `scikit-learn` estimator after using `predict_proba()`.
        - `unique_labels`: Unique labels included in `map`. Tip: Unique labels should be the same
        as those used to train the model that classified the map (`y_train`).
        """

        self._cube_shape = cube_shape
        self._pred_map = map
        self._unique_labels = unique_labels

        # To store the computed classification map with probabilities and binary
        self._map: NDArray[Any] = np.array(None)
        self._binary_map: NDArray[Any] = np.array(None)
        self._maps_computed = False

        self.__compute_map()  # Compute map

    @property
    def map(self) -> NDArray[Any]:
        """
        Class property that returns the computed probabilistic classification map with 3 channels (R,G,B).

        It returns an array of shape (rows, columns, 3)
        """
        return self._map

    @property
    def binary_map(self) -> NDArray[Any]:
        """
        Class property that returns the computed binary classification map with 3 channels (R,G,B).

        It returns an array of shape (rows, columns, 3)
        """
        return self._binary_map

    def plot(
        self,
        title: str,
        show_axis: bool = False,
        path_: str = "./",
        file_suffix: str = "suffix",
        file_format: str = "png",
    ) -> Union[List[Figure], None]:
        """
        Save the computed classification map. It does nothing if the map has not been computed.
        Additionally, it can also show the plot

        Parameters
        ----------
        - `title`: Title of the plot.
        - `show_axis`: Flag to show the coordenates in all axis of the plot
        - `path_`: Path to save the bar plot in disk memory.
        - `file_suffix`: String to use as suffix to differentiate saved files.
        - `file_format`: File extension when saving the figure. (E.g. '.png', '.svg').
            - Supported formats: `eps`, `jpeg`, `jpg`, `pdf`, `pgf`, `png`, `ps`, `raw`, `rgba`, `svg`, `svgz`, `tif`, `tiff`.

        Returns
        -------
        List with both classification maps as `matplotlib.figure.Figure` objects.
        First probabilistic map and second the binary map.
        """
        # Plot the maps if it has been computed
        if not self._maps_computed:
            return None

        binary_map = {
            "id": "Binary",
            "cls_map": self._binary_map,
        }

        proba_map = {
            "id": "Probabilistic",
            "cls_map": self._map,
        }

        map_figures: List[Figure] = []

        # Plot and save both binary and probabilistic classification maps
        for classification_map in [proba_map, binary_map]:

            fig = plt.figure()
            plt.title(f"{title} - {classification_map['id']} map")
            plt.imshow(classification_map["cls_map"])

            # Use this to stop showing coordenate axis for the GT map
            if not show_axis:
                plt.axis("off")

            plt.tight_layout()  # Resize layout so nothing is cropped in the image

            path_ = check_path(path_)
            save_path = (
                f"{path_}ClassificationMap_{classification_map['id']}_{file_suffix}.{file_format}"
            )
            plt.savefig(save_path, bbox_inches="tight")

            map_figures.append(fig)
            plt.close()

        return map_figures

    def __compute_map(self) -> None:
        """
        Generates a color map by translating each label value to an RGB value.
        It generates both the probability map as well as the binary map.
        """

        # Get all label references
        label_refs: NDArray[Any] = np.array([int(label) for label in HSI_LABEL_INFO.keys()])

        # Get all label color references
        label_colors = (
            np.array(
                [
                    HSI_LABEL_INFO[str(label)]["Color"]
                    for label in label_refs
                    if label in self._unique_labels
                ]
            )
            / 255.0
        )

        # * Compute probability map
        colored_proba_pixels: NDArray[Any] = np.matmul(self._pred_map, label_colors)
        self._map = colored_proba_pixels.reshape(self._cube_shape[0], self._cube_shape[1], 3)

        self._maps_computed = True

        # * Compute and store binary map
        max_val = np.amax(self._pred_map, axis=1, keepdims=True)
        colored_pixels: NDArray[Any] = np.matmul(self._pred_map // max_val, label_colors)
        self._binary_map = colored_pixels.reshape(self._cube_shape[0], self._cube_shape[1], 3)

        self._maps_computed = True
