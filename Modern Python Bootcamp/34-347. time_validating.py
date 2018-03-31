import re


def is_valid_time(s):
    pattern = re.compile(r'^[1,2]?\d:[0-5]\d$')
    result = pattern.search(s)
    if result:
        return True
    return False
