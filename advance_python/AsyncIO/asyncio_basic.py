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


# asyncio.run(main_gather())


# Synchronization primitives
async def producer(q):
    for i in range(5):
        # await asyncio.sleep(1)
        await q.put(i)
        print("produced", i)
    await q.join()


async def consumer(q):
    while True:
        item = await q.get()
        print("consumed", item)
        q.task_done()


async def pipeline():
    q = asyncio.Queue()
    # gather will not kill the consumer as there is no exit condition
    # results = await asyncio.gather(producer(q), consumer(q))

    cons_task = asyncio.create_task(consumer(q))
    await producer(q)
    await q.join()
    cons_task.cancel()


# asyncio.run(pipeline())

# Running blocking code in asyncio


def blocking_io(x):
    import time

    time.sleep(2)
    return x


async def call_blocking_io():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, blocking_io, 5)
    print(result)


asyncio.run(call_blocking_io())
