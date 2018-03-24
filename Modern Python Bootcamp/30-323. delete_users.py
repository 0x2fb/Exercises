import csv


def delete_users(first_name, last_name):
    with open("users.csv", "r") as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    count = 0
    with open("users.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        for row in users:
            if row[0] == first_name and row[1] == last_name:
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)
