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
        a = input("Please enter an integer ")
        if a == "q":
            break
        try:
            print(a ** 2)
        except TypeError:
            print("Invalid input")


ask()
