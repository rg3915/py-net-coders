import csv

with open('users.csv') as f:
    users_reader = csv.reader(f)
    for row in users_reader:
        print(row)
