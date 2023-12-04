"""
Utilities for parsing input files from Advent of Code.
"""
from __future__ import annotations

from typing import Any, List


def read_input(path: str) -> List[Any]:
    """
    Read the input file at the given path and return a list of the lines.
    """
    input_strings = open(path).readlines()
    return [line.strip() for line in input_strings]


def read_input_as_grid(filepath: str) -> List[List[int]]:
    """
    Parse the input data into a list of integers
    """
    with open(filepath) as f:
        grid = []
        for line in f.readlines():
            grid.append(list(map(int, line.strip())))
    return grid
