#!/usr/bin/env python3
"""Async generator module"""

import asyncio
import random

async def async_generator():
    """Async generator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def async_comprehension():
    """Collects 10 random numbers using async comprehension over async_generator"""
    return [i async for i in async_generator()]
