"""
CASE 4
Are there differences in activity patterns between weekdays and weekends?
    1. Create a new factor variable in the dataset with two levels - "weekday" and "weekend" indicating whether a given date is a weekday or weekend day.
    2. Make a plot containing a time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all weekdays or weekend days (y-axis).
"""
import csv
import statistics as st
import pandas as pd
import pygal
import matplotlib.pyplot as plt
import datetime

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    wr = open('newActivity.csv','w')
    wr.write(str(headerRow[0])+","+str(headerRow[1]+","+str(headerRow[2])))
    wr.write("\n")
    
    n = 0
    for row in reader:
        if(row[0] == 'NA'):
            row[0] = 0
            n += 1
        if pd.to_datetime(row[1]).weekday() >= 5:
            day = "Weekend"
        else:
            day = "Weekday"
            
        wr.write(str(row[0])+","+str(row[1])+","+str(row[2])+","+str(day))
        wr.write("\n")
    wr.close()
    
filename = 'newActivity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)

    dictDate = {}
    dictInterval = {}
    dictInterWeekday = {}
    dictInterWeekend = {}
    
    for row in reader:
        steps = row[0]
        date = row[1]
        interval = int(row[2])
        day = row[3]

        dictDate.setdefault(str(date),[])
        dictDate[str(date)].append(int(steps))  #adds steps per day
            
        dictInterval.setdefault(interval,[])
        dictInterval[interval].append(int(steps)) #adds steps per interval

        if day == "Weekday":
            dictInterWeekday.setdefault(interval, [])
            dictInterWeekday[interval].append(int(steps))
        elif day == "Weekend":
            dictInterWeekend.setdefault(interval, [])
            dictInterWeekend[interval].append(int(steps))
    
    listInterval = []
    listAveSteps = []
    listAveStepsWeekday = []
    listAveStepsWeekend = []

    for i in dictInterval.keys():
        listInterval.append(i)
        listAveSteps.append(round(st.mean(dictInterval.get(i)), 2))

    for i in dictInterWeekday.keys():
        listAveStepsWeekday.append(round(st.mean(dictInterWeekday.get(i)), 2))

    for i in dictInterWeekend.keys():
        listAveStepsWeekend.append(round(st.mean(dictInterWeekend.get(i)), 2))

    hist = pygal.Bar()
    hist.title = "Average Steps across Weekdays and Weekends"
    hist.x_title = "5 minute intervals"
    hist.x_labels = listInterval
    hist.y_title = "Average Steps"
    hist.add("Weekdays", listAveStepsWeekday)
    hist.add("Weekends", listAveStepsWeekend)
    hist.render_to_file('AverageStepsWeekdayWeekend.svg')

    # plt.plot(sorted(listInterval), listAveStepsWeekday, label="weekday")
    # plt.plot(sorted(listInterval), listAveStepsWeekend, label="weekend")
    # plt.legend()
    # plt.show()