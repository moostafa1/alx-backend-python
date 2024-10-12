#!/usr/bin/env python3
"""
datatype annotated function
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    k: string value
    v: int or float value

    Return: the string and the square of the int or float value
    """
    return (k, v ** 2)
