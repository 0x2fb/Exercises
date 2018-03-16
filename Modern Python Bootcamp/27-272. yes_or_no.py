def yes_or_no():
    while True:
        yield 'yes'
        yield 'no'


# infinite loop
for i in yes_or_no():
    print(i)
