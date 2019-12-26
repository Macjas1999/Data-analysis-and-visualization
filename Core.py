import csv

with open('masterCSV.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        print(row[0])
        print(row[1])
        print(row[2])
