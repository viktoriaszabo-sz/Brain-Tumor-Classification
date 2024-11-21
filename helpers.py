#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Helpers functions useful for the entire package

    -------------------------------------------------------------------------
    AUTHOR

    Name:       Alberto Martín Pérez
    Contact:    a.martinp@upm.es

    ------------------------------------------------------------------------
    SUMMARY

    Useful functions for various purposes for program executions.
   """

import os
from sys import platform


def check_path(path_: str) -> str:
    """
    Checks if given path exists in disk memory. If it does not exist, it creates it.
    Returns the path in case it does not end with `/` or `\\`.

    Parameters
    ----------
    - `path_`:  Path to check if exist in disk memory. Creates it if does not exist.

    Reference
    ---------
    - To create intermediate folders, the solution was based on:
        https://stackoverflow.com/questions/59181118/os-mkdir-returns-error-filenotfounderror-errno-2-no-such-file-or-directory
    """
    # Linux uses '/' for directories
    if platform == "linux" or platform == "linux2":
        if not path_.endswith("/"):
            path_ = f"{path_}/"

    # Windows uses '\' for directories
    elif platform == "win32":
        if not path_.endswith("\\"):
            path_ = f"{path_}\\"

    # Create path if it does not exist
    if not os.path.exists(path_):
        os.makedirs(os.path.join(path_))

    return path_


def check_format(string_: str) -> str:
    """
    Checks if given string contains file format and removes it.

    Parameters
    ----------
    - `string_`:  String to check if contains a file format.
    """

    if "." in string_:
        string_, format_ = string_.split(".", 1)

    return string_
