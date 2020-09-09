import time
from functools import wraps

def cal_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} function took {end - start:.5f} s")
        return result
    return wrapper

