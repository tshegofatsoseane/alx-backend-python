#!/usr/bin/env python3
"""Measures the time"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes the async_comprehension function four times in parallel
        and measure_runtime should measure the total runtime and return it"""
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - start_time
