import csv

crimes = [row[5] for row in csv.reader(open("Crimes.csv")) if "2015" in row[2]]
print(max(set(crimes), key=lambda x: crimes.count(x)))

# from collections import Counter
# print(Counter(crimes).most_common()[0])