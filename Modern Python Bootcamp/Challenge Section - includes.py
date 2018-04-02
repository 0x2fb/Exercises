def includes(collection, num, i=0):
    if type(collection) == dict:
        return num in collection.values()
    else:
        return num in collection[i:]


print(includes([1, 2, 3], 1))  # True
print(includes([1, 2, 3], 1, 2))  # False
print(includes({'a': 1, 'b': 2}, 1))  # True
print(includes({'a': 1, 'b': 2}, 'a'))  # False
print(includes('abcd', 'b'))  # True
print(includes('abcd', 'e'))  # False
