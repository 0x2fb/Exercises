import csv


def update_users(old_first_name, old_last_name, new_first_name, new_last_name):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        users = list(csv_reader)

    count = 0
    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in users:
            if row[0] == old_first_name and row[1] == old_last_name:
                csv_writer.writerow([new_first_name, new_last_name])
                count += 1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}.".format(count)
