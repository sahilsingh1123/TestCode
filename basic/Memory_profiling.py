"""
Memory profiling could be done with multiple options
- tracemalloc
- cprofile
- mem_tools
"""

import tracemalloc

"""Using the tracemalloc for memory profiling"""


def sum_mem():
    print("sum_mem called")
    li = []
    for i in range(1000):
        li.append(i)

    return li


tracemalloc.start()

val = sum_mem()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")
[print(stat) for stat in top_stats]

"""
comparing before and after
- we can also filter the snapshots based on criteria
"""


def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)


tracemalloc.start()
snap1 = tracemalloc.take_snapshot()
fib(40)
snap2 = tracemalloc.take_snapshot()

top_stats = snap2.compare_to(snap1, "lineno")

for stat in top_stats:
    print(stat)
