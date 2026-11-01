import matplotlib.pyplot as plt

animals =[]
count = []

with open('animal_counts_large.csv') as csvfile:
    content = csvfile.readlines()

    #spring en linje over
    #next(csvfile)
    for row in content:
        newrow = row.split(',')
        animals.append(newrow[0])
        count.append(int(newrow[1]))

plt.pie(count, labels=animals, autopct='%1.1f%%',pctdistance=1, labeldistance=1.2)
plt.title("zoo animals")
plt.show()