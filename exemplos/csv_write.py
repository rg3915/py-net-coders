import csv

with open('file.csv', 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow([1, 'Um', 'One'])
    extra_rows = [[2, 'Dois', 'Two'], [3, 'Três', 'Three']]
    csv_writer.writerows(extra_rows)
