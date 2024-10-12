#!/usr/bin/env python3
from typing import List, Union

"""
datatype annotated function
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    mxd_lst: list of int and float values

    Return: sum of all values of the list
    """
    return sum(mxd_lst)
