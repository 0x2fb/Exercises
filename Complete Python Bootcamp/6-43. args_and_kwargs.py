def myargs(*args):
    return sum(args)


def even_args(*args):
    return [i for i in args if i % 2 == 0]


def alternate(s):
    return ''.join([l.upper() if i % 2 != 0 else l for i, l in enumerate(s.lower())])
