import functools


# This is amazing!
# From: https://realpython.com/primer-on-python-decorators/
def cache(func):
    """Keep a cache of previous function calls"""

    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = dict()
    return wrapper_cache


# @cache
# This decorator below is python standard library version (better version of cache above)
@functools.lru_cache(maxsize=4)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    # misses=11 (10-0), hits=8 (8-1)
    print(f"Running fibonacci(10)")
    fibonacci(10)

    # misses=0 , hits=1 (8)
    # fibonacci(10, 9, 8, 7) known from before
    print(f"Running fibonacci(8)")
    fibonacci(8)

    # misses=6 (5-0), hits=3 (3-1)
    # fibonacci(10, 9, 8, 7) known from before
    print(f"Running fibonacci(5)")
    fibonacci(5)

    # misses=3 (8-6), hits=4 (6,5,5,4)
    # fibonacci(5, 4, 3, 2) known from before
    print(f"Running fibonacci(8)")
    fibonacci(8)

    # misses=0, hits=1 (5)
    # fibonacci(8, 7, 6, 5) known from before
    print(f"Running fibonacci(5)")
    fibonacci(5)

    # misses=11+0+6+3+0=20, hits=8+1+3+4+1=16
    print(f"Running print(fibonacci.cache_info)")
    print(fibonacci.cache_info())
