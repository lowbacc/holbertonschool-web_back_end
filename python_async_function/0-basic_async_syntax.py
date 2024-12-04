#!/usr/bin/env python3
""" Module that takes a float n as argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Asynchronous coroutine that takes an integer max_delay"""

    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
