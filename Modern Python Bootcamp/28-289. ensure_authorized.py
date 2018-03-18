from functools import wraps


def ensure_authorized(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any(k == 'role' and v == 'admin' for (k, v) in kwargs.items()):
            return fn(*args, **kwargs)
        return 'Unauthorized'
    return inner


@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"


print(show_secrets(role="admin"))  # "Shh! Don't tell anybody!"
print(show_secrets(role="nobody"))  # "Unauthorized"
print(show_secrets(a="b"))  # "Unauthorized"
