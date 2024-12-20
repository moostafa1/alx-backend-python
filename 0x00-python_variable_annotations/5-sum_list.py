#!/usr/bin/env python3
"""
datatype annotated function
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    input_list: list of float values

    Return: sum of all values of the list
    """
    return sum(input_list)
