import csv
from matplotlib import pyplot as plt
from numpy import datetime64

filename = "sitka_weather_2014.csv" #file in github folder
with open(filename) as f:
    reader = csv.reader(f)
    headRow = next(reader)
    print(headRow)

    for i, colHead in enumerate(headRow):
        print(i, colHead)
    
    # Extracts high temperature from the file
    dates, highs = [], []
    for row in reader:
        cDate = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(cDate)

        high = int(row[1])
        highs.append(high)
    print(highs)

    # Get average high temperature from the file
    averageHighTemp = sum(highs) / len(highs)
    print(averageHighTemp)

# Plotting the high temperatures
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c="red")
plt.title("Daily High Temperatures", fontsize=15)
plt.xlabel("", fontsize=10)
plt.ylabel("Temperature (F)", fontsize=10)
plt.show()