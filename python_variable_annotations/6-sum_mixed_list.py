#!/usr/bin/env python3
""" Module that takes a list of mixed types as argument"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Function that takes a list of mixed types as argument"""

    return sum(mxd_lst)
