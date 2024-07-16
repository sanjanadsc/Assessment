
import time
import logging

logging.basicConfig(level=logging.INFO)

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Function {func.__name__} took {end_time - start_time} seconds")
        return result
    return wrapper

@timing_decorator
def expensive_function(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total
