def get_unlimited_multiples(num=1):
    count = 1
    while True:
        yield num * count
        count += 1


sevens = get_unlimited_multiples(7)
print([next(sevens) for i in range(15)])

ones = get_unlimited_multiples()
print([next(ones) for i in range(20)])
