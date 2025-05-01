"""
map() function
- when we have to apply some transformation on any iterables
  (ex-list,tuples,....), we can use map(transformation_function, iterables)
"""


def sqaure(number):
    return number**2


nums = [1, 2, 3, 4, 5, 6]

data = map(sqaure, nums)
"""
by default = map will return a map Object, and you can iterate over it
using for loop or you can call the __next__() method.

- if want the return object in list - pass list(map(func, iterables))

"""
data = map(str, nums)

data = map(lambda x: x**2, nums)  # returns squared value

"""
with multiple iterables input
- make sure that many arguments must be accepted by the transformed function
"""

nums_2 = [2, 3, 4, 5, 6, 7]


def multiple(num1, num2):
    return num1 * num2


data = map(multiple, nums, nums_2)

"""
using filter() and map() together
calculate square root of positive integer only
"""
nums_negative = [2, 3, 4, 5, 6, 7, -3, -5, -9]


def is_positive(num):
    return num >= 0


data = map(sqaure, filter(is_positive, nums))

"""
using map() with reduce()
doubling the sum of all the value present in the list
after squaring it
"""

from functools import reduce


def double_sum(num1, num2):
    return (num1 + num2) * 2


data = reduce(double_sum, map(sqaure, nums))

print(dir(data))
