from functools import wraps
from time import sleep


def delay(seconds):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print('Waiting {}s before running {}'.format(seconds, fn.__name__))
            sleep(seconds)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hi():
    return "hi"


print(say_hi())
