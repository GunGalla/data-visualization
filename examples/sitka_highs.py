"""Sitka weather data."""
import csv

from matplotlib import pyplot as plt

filename = '/home/gungalla/Work/data-visualization/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Reads MAX temperature
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
    print(highs)

# Put data on diagram
plt.style.use('seaborn-v0_8-dark-palette')
fig, ax = plt.subplots()
ax.plot(highs, c='green')

# Diagram formatting
plt.title('Daily high temperatures, July 2018', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
