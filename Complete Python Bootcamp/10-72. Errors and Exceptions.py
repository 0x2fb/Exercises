for i in ['a', 'b', 'c']:
    try:
        print(i**2)
    except TypeError:
        print("No strings supported with this operator")

x = 5
y = 0

try:
    z = x / y
except ZeroDivisionError:
    print("Can't divide by zero")


def ask():
    while True:
        try:
            a = int(input("Please enter an integer "))
        except ValueError:
            print("Invalid input")
            continue
        print(a ** 2)


ask()
