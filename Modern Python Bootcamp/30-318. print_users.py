import csv


def print_users():
    with open("users.csv", 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            print("{} {}".format(row[0].title(), row[1].title()))
