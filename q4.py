import functools

def cache(func):
    """
    Custom cache decorator using functools.lru_cache.
    """
    return functools.lru_cache()(func)

# Example usage:
@cache
def expensive_function(n):
    """
    An expensive function that we want to cache.
    """
    # Simulate some expensive computation
    return n * 2

# Test the function with the same numbers
print(expensive_function(10))  # First call (computes and caches)
print(expensive_function(10))  # Second call (retrieves from cache)
print(expensive_function(20))  # New argument (computes and caches)

# Compare execution time patterns
