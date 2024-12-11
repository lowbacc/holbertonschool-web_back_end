#!/usr/bin/env python3
"""Async generator module"""

import asyncio
import random
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
