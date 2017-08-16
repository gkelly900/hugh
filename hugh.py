import csv
import numpy as np
import matplotlib.pyplot as plt

temp = []
precip_b = []
precip_w = []
year = []

with open('hugh_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile,)
    next(reader, None)
    for row in reader:
        try:
            year.append(float(row[0]))
        except(ValueError):
            year.append(None)
        try:
            precip_b.append(float(row[1]))
        except(ValueError):
            precip_b.append(None)
        try:
            precip_w.append(float(row[2]))
        except(ValueError):
            precip_w.append(None)
        try:
            temp.append(float(row[3]))
        except(ValueError):
            temp.append(None)


fig, ax1 = plt.subplots()

ax1.plot(year, precip_b, 'b-')
ax1.set_xlabel('Year')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('Precip Bunton', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(year, temp, 'r.')
ax2.set_ylabel('Temperature Fluctuation', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()
