#!/usr/bin/env python3
""" Module that takes an integer n and an integer max_delay as arguments"""

import asyncio
from typing import List
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes an integer max_delay"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Asynchronous coroutine that takes an integer n
    and an integer max_delay"""

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
