def two_list_dictionary(l1, l2):
    tld = {}
    for i, key in enumerate(l1):
        try:
            tld[key] = l2[i]
        except IndexError:
            tld[key] = None
    return tld


# {'a': 1, 'b': 2, 'c': 3, 'd': null}
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
# {'a': 1, 'b': 2, 'c': 3}
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]))
# {'x': 1, 'y': 2, 'z': null}
print(two_list_dictionary(['x', 'y', 'z'], [1, 2]))
