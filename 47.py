import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if "Computer" in row[1]:
            print(f" {row[0]}  {row[1]}  {row[2]}")
