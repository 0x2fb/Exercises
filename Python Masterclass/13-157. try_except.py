def get_int(text):
    while True:
        try:
            number = int(input(text))
            return number
        except ValueError:
            print("Invalid number entered.")


n1 = get_int("Please enter the first number ")
n2 = get_int("Please enter the second number ")

try:
    print("{} divided by {} is {}".format(n1, n2, n1 / n2))
except ZeroDivisionError:
    print("You can't divide by zero.")
