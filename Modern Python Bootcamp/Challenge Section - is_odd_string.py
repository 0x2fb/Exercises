import string


def is_odd_string(s):
    # count = 0
    # for i in s:
    #     count += string.ascii_lowercase.index(i.lower()) + 1
    # return False if count % 2 == 0 else True
    count = sum(string.ascii_lowercase.index(i.lower()) + 1 for i in s)
    return count % 2 != 0


print(is_odd_string('a'))  # True
print(is_odd_string('aaaa'))  # False
print(is_odd_string('Amazing'))  # True
print(is_odd_string('veryfun'))  # True
print(is_odd_string('veryfunny'))  # False
