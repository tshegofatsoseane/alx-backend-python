#!/usr/bin/env python3
""" Complex types - string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes string k and int OR float v as arguments
    then returns a tuple.
    """

    return (k, v**2)
