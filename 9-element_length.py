#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence

"""
datatype annotated function
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
    lst: An iterable containing sequences (like strings, lists, tuples, etc.)

    Returns:
    A list of tuples, where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
