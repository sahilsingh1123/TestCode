"""
This file contains the code snippet for functools lib
"""

import functools
from functools import wraps

"""
import time
from datetime import datetime, timedelta
_time_format = "%Y-%m-%d %H"

def _normalize_time_range(start_time, end_time):
    ranges = list()
    delta = timedelta(hours=1)
    while end_time - start_time >= delta:
        _end_time = start_time + delta
        ranges.append((start_time, _end_time))
        start_time = _end_time
    return ranges

def get_older_time(**kwargs):
    return timedelta(**kwargs)

_end_last_run = datetime.utcfromtimestamp(time.time() - 691200)
floor_end_time_last_run = _end_last_run.strftime(_time_format)
_end_time_last_run = datetime.strptime(floor_end_time_last_run, _time_format)
print(_end_time_last_run)

now = datetime.utcfromtimestamp(time.time())
floor_now = now.strftime(_time_format)
now_final = datetime.strptime(floor_now, _time_format)
print(now_final)

# initial_time_range = timedelta(days=7)
initial_time_range = get_older_time(days=6, hours=23)
_now_seven_days = now_final - initial_time_range
print(_now_seven_days)
if _now_seven_days > _end_time_last_run:
    final_start_date = _now_seven_days
    print("yes, exceeded 7 days")


# for start_t,end_t in _normalize_time_range(_start_time, _end_time):
#     print(f"start - {start_t}")
#     print(f"end - {end_t}")

"""

print("start")


def _wrapper_func(func):
    @wraps(func)
    def _wrap_func(*args, **kwargs):
        print("inside wrap_func")
        func.inside_test()
        return func(*args, **kwargs)

    return _wrap_func


def _wrapper_func_2(func):
    @wraps(func)
    def _wrap_func(*args, **kwargs):
        print("inside wrap_func2")
        return func(*args, **kwargs)

    return _wrap_func


@_wrapper_func_2
@_wrapper_func
def test(val: str, val2: str):
    print(f"inside test method, val: {val}")
    print(f"inside test method, val2: {val2}")

    def inside_test():
        print("inside inside test-func")


test(1, 2)
