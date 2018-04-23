import math
import string


def vol(rad):
    return (4 / 3) * (math.pi * (rad ** 3))


print(vol(2))
print("=" * 50)


def ran_check(num, low, high):
    if num in tuple(range(low, high)):
        return f'{num} is in the range between {low} and {high}.'
    else:
        return f'{num} is not in the range between {low} and {high}.'


def ran_bool(num, low, high):
    return num in tuple(range(low, high))


print(ran_check(5, 2, 7))
print(ran_bool(3, 1, 10))
print("=" * 50)


def up_low(s):
    s_up = 0
    s_low = 0
    for i in s:
        if i.isupper():
            s_up += 1
        elif i.islower():
            s_low += 1
    print(f"No. of Upper case character: {s_up}.")
    print(f"No. of Lower case character: {s_low}.")


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')
print("=" * 50)


def unique_list(ls):
    return list(set(ls))


print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))
print("=" * 50)


def multiply(numbers):
    result = 1
    for i in numbers:
        result *= i
    return result


print(multiply([1, 2, 3, -4]))
print("=" * 50)


def palindrome(s):
    return s == s[::-1]


print(palindrome('helleh'))
print("=" * 50)


def ispangram(s, alphabet=string.ascii_lowercase):
    # return all([i.lower() in alphabet for i in set(strl)])
    return all([i.lower() in alphabet for i in set(s.lower()) if i.lower() in alphabet])


print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("The five boxing wizards jump quickly."))
