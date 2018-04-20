import math


def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))
print('-' * 50)


def animal_crackers(s):
    a, b = s.split()
    return a[0].lower() == b[0].lower()


print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))
print('-' * 50)


def makes_twenty(a, b):
    if a == 20 or b == 20:
        return True
    else:
        return sum((a, b)) == 20


print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print('-' * 50)


def old_macdonald(name):
    return ''.join((l.upper() if i == 0 or i == 3 else l.lower()for i, l in enumerate(name)))


print(old_macdonald('macdonald'))
print('-' * 50)


def master_yoda(s):
    return ' '.join(reversed(s.split()))


print(master_yoda('I am home'))
print(master_yoda('We are ready'))
print('-' * 50)


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
print('-' * 50)


def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print('-' * 50)


def paper_doll(s):
    return ''.join((i * 3 for i in s))


print(paper_doll("Hello"))
print(paper_doll('Mississippi'))
print('-' * 50)


def blackjack(a, b, c):
    nums = [a, b, c]
    if sum(nums) <= 21:
        return sum(nums)
    for i in range(len(nums)):
        if nums[i] == 11:
            nums[i] = 1
    if sum(nums) <= 21:
        return sum(nums)
    else:
        return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
print('-' * 50)


def summer_69(nums):
    flag = True
    sum = 0
    for i in nums:
        if i == 6:
            flag = False
        if flag:
            sum += i
        if i == 9:
            flag = True
    return sum


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print('-' * 50)


def spy_game(arr):
    first = False
    second = False
    third = False
    for i in arr:
        if i == 0:
            first = True
        if first:
            if i == 0:
                second = True
        if second:
            if i == 7:
                third = True
    return all((first, second, third))


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
print('-' * 50)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def prime_generator(n):
    for i in range(n):
        if is_prime(i):
            yield i


def count_primes(n):
    return len(tuple(prime_generator(n)))


print(count_primes(100))
