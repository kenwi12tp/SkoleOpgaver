import csv

import matplotlib.pyplot as plt

animals =[]
count = []

with open('animal_counts_large.csv', newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        animals.append(row[0])
        count.append(int(row[1]))

plt.pie(count, labels=animals, autopct='%1.1f%%',pctdistance=1, labeldistance=1.2)
plt.title("zoo animals")
plt.show()