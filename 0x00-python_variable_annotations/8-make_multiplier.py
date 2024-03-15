#!/usr/bin/env python3
""" Complex types functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as and argument,
    then returns a function that multiplies float number by multiplier.
    """
    def f(n: float) -> float:
        """ multiplies a float by multiplier """
        return float(n * multiplier)

    return f
