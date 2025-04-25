"""
This file will contain basic details about
asyncio module
"""

import asyncio
import time

async def fetch_data(x):
    await asyncio.sleep(1)
    return x * 2

async def main_1():
    # schedule fetch_data as task
    task = asyncio.create_task(fetch_data(10))
    result = await task
    print(result)

# asyncio.run(main_1())
async def worker(id):
    start = time.perf_counter()
    await asyncio.sleep(id)
    elapsed = time.perf_counter() - start
    print(f"worker {id} took {elapsed:.3f}s")
    return f"worker {id} done"

async def main_gather():
    # gather
    results = await asyncio.gather(*(worker(i) for i in range(10)))
    print(results)

    # structured concurrency
    # results = await asyncio.gather(*(worker(i) for i in range(10)), return_exceptions=True)
    # print(results)


asyncio.run(main_gather())