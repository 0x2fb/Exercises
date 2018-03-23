import csv


def add_user(first_name, last_name):
    with open("users.csv", 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow([first_name, last_name])
