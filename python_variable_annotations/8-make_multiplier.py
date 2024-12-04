#!/usr/bin/env python3
""" Module that takes a float multiplier as argument"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Function that takes a float multiplier as argument"""

    def multiplier_function(value: float) -> float:
        """ Function that takes a float value as argument"""

        return value * multiplier
    
    return multiplier_function
