from functools import wraps


def show_args(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Here are the args:", tuple((i for i in args)))
        print("Here are the kwargs:",
              {k: v for (k, v) in kwargs.items()})
        return fn(*args, **kwargs)
    return wrapper


@show_args
def do_nothing(*x, **y):
    pass


do_nothing(1, 2, 3, a="hi", b="bye")
