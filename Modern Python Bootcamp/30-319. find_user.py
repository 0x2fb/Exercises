import csv


def find_user(first_name, last_name):
    with open("users.csv", 'r') as file:
        csv_reader = list(csv.reader(file))
        try:
            result = csv_reader.index([first_name, last_name])
            return result
        except ValueError:
            return "{} {} not found.".format(first_name, last_name)
