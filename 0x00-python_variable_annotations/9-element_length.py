#!/usr/bin/env python3
""" Let duck type an iterable object"""
from typing import Mapping, MutableMapping, Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns element length """
    return [(i, len(i)) for i in lst]
