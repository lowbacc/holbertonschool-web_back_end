#!/usr/bin/env python3
"""Async generator module"""

import asyncio
import random
import time
from typing import Generator
from typing import List


async def async_generator() -> Generator[float, None, None]:
    """Async generator function"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> list[float]:
    """Collects 10 random numbers using async comprehension
    over async_generator"""

    return [i async for i in async_generator()]


async def measure_runtime() -> float:
    """Measures the total runtime of executing
    async_comprehension four times in parallel"""

    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
