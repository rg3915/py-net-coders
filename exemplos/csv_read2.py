import csv

with open('users.csv') as f:
    users_reader = csv.DictReader(f)
    for row in users_reader:
        print(row['id'], row['username'], row['email'])
