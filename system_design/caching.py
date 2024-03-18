"""
Multiple ways of achieving caching in our system

1. Redis
2. Memcached
3. DynamoDB

"""

# lru_cache
from functools import lru_cache

@lru_cache(maxsize=100)
def expensive_function(param):
    # Time-consuming computation or database query
    return "result"


# diskcache
import diskcache as dc

cache = dc.Cache('./cache_directory')

def expensive_function(param):
    if param not in cache:
        # Expensive computation or database query
        cache[param] = "result"
    return cache[param]


# memcache
'''
For distributed applications or when you need a shared cache across multiple processes or servers,
using a caching system like Redis or Memcached can be ideal. These systems run as
a separate services and can be interacted with using Python clients.
'''
import memcache
import redis

mc = memcache.Client(['127.0.0.1:11211'], debug=0)
r = redis.Redis(host='localhost', port=6379, db=0)

def expensive_function(param):
    result = r.get(param)
    if result is None:
        # Expensive computation or database query
        r.set(param, result)
    return result
