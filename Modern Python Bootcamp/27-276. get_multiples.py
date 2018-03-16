def get_multiples(num=1, count=10):
    val = 1
    while val <= count:
        yield num * val
        val += 1
    raise StopIteration


for i in get_multiples(4):
    print(i)
print('-' * 40)
for i in get_multiples(4, 3):
    print(i)
