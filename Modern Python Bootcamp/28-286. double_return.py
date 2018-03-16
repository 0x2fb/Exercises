def double_return(fn):
    def wrapper(*args, **kwargs):
        val = fn(*args, **kwargs)
        return [val, val]
    return wrapper


@double_return
def add(x, y):
    return x + y


add(1, 2)


@double_return
def greet(name):
    return "Hi, I'm " + name


greet("Kyle")
