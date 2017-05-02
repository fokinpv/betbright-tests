"""Least recently used cache.
Implement a least recently used (LRU) cache mechanism using a
decorator and demonstrate it use in a small script. The LRU must be
able to admit a 'max_size' parameter that by default has to be 100.
"""
import time
from functools import wraps


def lru(max_size=100):

    class _item:
        __slots__ = ('last_used', 'value')

        def __init__(self, value=None):
            self.last_used = time.time()
            self.value = value

        def __repr__(self):
            return '<_item {0.last_used} {0.value}>'.format(self)

    _cache = {}

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            #  args_hash = hash(
            #      args + (object(),) + tuple(sorted(kwargs.items()))
            #  )
            args_hash = hash(args + tuple(sorted(kwargs.items())))

            if len(_cache) == max_size:
                key, _ = min(
                  _cache.items(), key=lambda item: item[1].last_used
                )
                del _cache[key]

            if args_hash in _cache:
                item = _cache[args_hash]
                item.last_used = time.time()
                return item.value
            else:
                _cache[args_hash] = _item()
                func_result = func(*args, **kwargs)
                # If we call decorated function recursively,
                # it can be removed from cache due to max_size exceeded.
                if args_hash in _cache:
                    _cache[args_hash].value = func_result
                return func_result

        def cache_len():
            return len(_cache)

        wrapper.cache_len = cache_len
        wrapper._cache = _cache

        return wrapper
    return decorator
