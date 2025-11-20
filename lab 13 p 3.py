import csv

with open(r'C:\Users\chira\Downloads\data-1.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
