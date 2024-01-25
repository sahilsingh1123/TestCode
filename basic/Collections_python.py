# https://docs.python.org/3/library/collections.html
from collections import ChainMap, Counter, deque

print("Creating this for testing all the collections types and actions")

"""
ChainMap
The ChainMap creates a list of dictionaries or mappings
and allows you to perform lookups on them as if they were a 
single dictionary. When you do a lookup, it will search 
each dictionary in the chain in order, returning the first value it finds.
"""

default_config = {'debug': False, 'log_level': 'INFO'}
user_config = {'log_level': 'DEBUG'}

chained_dict = ChainMap(user_config, default_config)
print(chained_dict["log_level"])

"""
Counter
A Counter is a dict subclass for counting hashable objects. 
It is a collection where elements are stored as dictionary keys 
and their counts are stored as dictionary values. Counts are allowed 
to be any integer value including zero or negative counts. 
The Counter class is similar to bags or multisets in other languages.
"""

c = Counter()
for word in ["red", "blue", "red", "green", "red"]:
    c[word] += 1

c = Counter("aabbbssssccccd")
print(c["a"])  # => return 2
print(c.most_common())  # => {s=4, c=4, b=3....}

"""
Deques ("Deck")
Deques are a generalization of stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.
Though list objects support similar operations, they are optimized for fast fixed-length operations and incur O(n) memory movement costs for pop(0) and insert(0, v) operations which change both the size and position of the underlying data representation.
If maxlen is not specified or is None, deques may grow to an arbitrary length. Otherwise, the deque is bounded to the specified maximum length. Once a bounded length deque is full, when new items are added, a corresponding number of items are discarded from the opposite end. Bounded length deques provide functionality similar to the tail filter in Unix. They are also useful for tracking transactions and other pools of data where only the most recent activity is of interest.
"""

stack = deque(maxlen=3)
for i in range(10):
    stack.append(i)

"""
DefaultDict
defaultdict is a subclass of Python's built-in dictionary that overrides one method, __missing__, to provide a default value for a nonexistent key. The default value is specified when creating the defaultdict object.
"""

from collections import defaultdict

fruits = defaultdict(lambda: 'unknown')
fruits['apple'] = 'red'
fruits['banana'] = 'yellow'

print(fruits['apple'])  # output: 'red'
print(fruits['banana'])  # output: 'yellow'
print(fruits['orange'])  # output: 'unknown

# ex - 2
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)  # here now u can perform list operation for value.

sorted(d.items())

# ex - 3

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())

"""
namedTuple

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
p[0] + p[1]             # indexable like the plain tuple (11, 22)
33
x, y = p                # unpack like a regular tuple
x, y
(11, 22)
p.x + p.y               # fields also accessible by name
33
p                       # readable __repr__ with a name=value style
Point(x=11, y=22)
"""
from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

Point = namedtuple('Point', ['x', 'y'])
t = [11, 22]
Point._make(t)
Point(x=11, y=22)


"""
OrderedDict
Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations. They have become less important now that the built-in dict class gained the ability to remember insertion order (this new behavior became guaranteed in Python 3.7).

- The OrderedDict algorithm can handle frequent reordering operations better than dict. As shown in the recipes below, this makes it suitable for implementing various kinds of LRU caches.
- A regular dict does not have an efficient equivalent for OrderedDict’s od.move_to_end(k, last=False) which moves the key and its associated value to the leftmost (first) position.

"""
from collections import OrderedDict
from time import time

class TimeBoundedLRU:
    "LRU Cache that invalidates and refreshes old entries."

    def __init__(self, func, maxsize=128, maxage=30):
        self.cache = OrderedDict()      # { args : (timestamp, result)}
        self.func = func
        self.maxsize = maxsize
        self.maxage = maxage

    def __call__(self, *args):
        if args in self.cache:
            self.cache.move_to_end(args)
            timestamp, result = self.cache[args]
            if time() - timestamp <= self.maxage:
                return result
        result = self.func(*args)
        self.cache[args] = time(), result
        if len(self.cache) > self.maxsize:
            self.cache.popitem(0)
        return result