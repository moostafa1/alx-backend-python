#!/usr/bin/env python3
"""
datatype annotated function
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
    multiplier: A float value to multiply by

    Returns:
    A function that takes a float and returns the product of it and the
    multiplier
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
