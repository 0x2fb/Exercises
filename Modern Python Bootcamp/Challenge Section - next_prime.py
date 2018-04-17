import math


def next_prime():
    next_prime.counter = 2

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    while True:
        if is_prime(next_prime.counter):
            yield next_prime.counter
        next_prime.counter += 1


primes = next_prime()
print([next(primes) for i in range(25)])
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
