import csv
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import numpy as np

# more or less how to make a excel fil lignende ting
animals = []
count = []
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#fig = go.Figure(data=[go.Table(
#    header=dict(values=["Navn", "Alder"]),
#    cells=dict(values=[["Alice", "Bob"], [25, 30]])
#)])

#fig.show()
with open('animal_counts_large.csv', newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        animals.append(row[0])
        count.append(int(row[1]))

animals_plot = go.Figure(data=[go.Table(
    header=dict(values=["Animal", "Count"]),
    cells=dict(values=[animals, count])
)
]
)
animals_plot.update_layout(
    title="zoo animals")
animals_plot.show()

#barchart
animals_plot_bar = go.Figure(data=[go.Bar(
    x=animals,
    y=count,
    marker_color=["red", "green", "blue"],

)]
)
animals_plot_bar.update_layout(
    title="zoo animals",
    xaxis_title="Animals",
    yaxis_title="Count", )
animals_plot_bar.show()

#matplot bar
plt.rcParams["figure.figsize"] = [20, 5]
plt.bar(animals, count)
plt.title("zoo animals")
plt.xlabel("Animals")
plt.ylabel("Count")
plt.show()

#punkt diagram (scatter plot)
plt.rcParams["figure.figsize"] = [20, 5]
plt.scatter(animals, count)
plt.title("zoo animals")
plt.xlabel("Animals")
plt.ylabel("Count")

plt.show()


#scatter med tedens linje skal bestå af 2 værdier der består af tal
a,b = np.polyfit(number, count, 1)
plt.rcParams["figure.figsize"] = [20, 5]
plt.scatter(number, count)
plt.title("zoo animals")
plt.xlabel("Animals")
plt.ylabel("Count")

plt.plot(number, [a*t + b for t in number])
plt.show()

#piechart
plt.pie(count, labels=animals, autopct='%1.1f%%')
plt.title("zoo animals")
plt.show()

#histogram
values= [1,2,3,4,3,3,3,2,2,1,1,5,5,6,7,7,6,6,5]
plt.hist(values)
plt.show()