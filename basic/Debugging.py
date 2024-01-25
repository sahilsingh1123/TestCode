# this is for testing different debugging tools for python code
import time
import pudb
import cProfile
import pstats
from memory_profiler import profile

'''
debugging the python code
'''

def test_debug_default():
    # https://docs.python.org/3/library/pdb.html
    val = 1
    print("before the break point")
    breakpoint()
    val = 2
    print("after the breakpoint")
    val = 3

# test_debug_default()


def test_debug_pudb():
    # https://documen.tician.de/pudb/usage.html#configuring-pudb
    pudb.set_trace()
    val = 1
    print("before the break point")
    val = 2
    print("after the breakpoint")
    val = 3
    for _ in range(val):
        t = _
    print("outside the loop")

#test_debug_pudb()

'''
Profiling in python code
'''

def test_profiling_cprofiler():
    print("start of function")
    time.sleep(5)
    print("end of function")

# with cProfile.Profile() as profile:
#     test_profiling_cprofiler()
# result = pstats.Stats(profile)
# result.sort_stats(pstats.SortKey.TIME)
# result.print_stats()
# result.dump_stats("profiling_result.prof")
# we can use tuna module to visualise the same in graph

'''Memory profiling'''

@profile()
def test_memory_profiler():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

test_memory_profiler()
'''
mprof can be used for plotting purposes
mprof run python file.py
mprof plot (make sure to install matplotlib)
'''
