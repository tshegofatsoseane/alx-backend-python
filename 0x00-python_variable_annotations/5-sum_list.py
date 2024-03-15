#!/usr/bin/env python3
""" Complex types list of floats """
from typing import Callable, Iterator, Union, Optional, List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list named input_list of floats as the argument
    then returns the sum as a float.
    """

    return sum(input_list)
