#!/usr/bin/env python3
""" Module that takes an integer n and an integer max_delay as arguments"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronous coroutine that takes an integer n and an integer max_delay"""

    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)

    return delays