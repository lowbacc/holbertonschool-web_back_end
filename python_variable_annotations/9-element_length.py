#!/usr/bin/env python3
""" Module that takes an iterable of sequences as argument"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Function that takes an iterable of sequences as argument"""

    return [(i, len(i)) for i in lst]
