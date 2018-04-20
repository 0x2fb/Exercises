def hello_world():
    print("Hello World")


def hello_name(name):
    print("Hello " + name)


def simple_boolean(b):
    if b is True:
        return "Hello"
    else:
        return "Goodbye"


def x_y_z(x, y, z):
    if z is True:
        return x
    else:
        return y


def sumab(a, b):
    return a + b


def is_even(n):
    if n % 2 == 0:
        return True
    return False
# def is_even(n):
#     return n % 2 == 0


def is_greater(a, b):
    return a > b
