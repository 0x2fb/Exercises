from functools import wraps


def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any(type(i) != int for i in args) is True or any(type(k) != int or type(v) != int for (k, v) in kwargs.items()) is True:
            return 'Please only invoke with integers.'
        else:
            return fn(*args, **kwargs)
    return inner


@only_ints
def add(x, y):
    return x + y


print(add(1, 2))  # 3
print(add("1", "2"))  # "Please only invoke with integers."
