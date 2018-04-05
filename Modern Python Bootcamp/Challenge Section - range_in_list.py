def range_in_list(ls, s=0, e=None):
    if e is None:
        return sum(ls[s:])
    return sum(ls[s:e + 1])
