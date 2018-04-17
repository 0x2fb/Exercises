def once(func):
    once.flag = True

    def inner(*args, **kwargs):
        if once.flag:
            once.flag = False
            return func(*args, **kwargs)
    return inner


def add(a, b):
    return a + b


oneAddition = once(add)

print(oneAddition(2, 2))  # 4
print(oneAddition(2, 2))  # None
print(oneAddition(12, 200))  # None
