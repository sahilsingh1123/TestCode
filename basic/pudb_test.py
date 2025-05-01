"""
This is a test code written for using pudb for debugging
in console directly
"""

import pudb


class PudbTest:
    def __init__(self):
        pass

    def test_func(self):
        v1 = "test1"
        v2 = "test3"
        # pudb.set_trace()
        combine = v1 + v2
        print(combine)


PudbTest().test_func()
