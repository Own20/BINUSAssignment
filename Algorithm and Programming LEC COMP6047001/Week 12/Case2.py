"""
    CASE 2
    What is the average daily activity pattern?
    1. Make a time series plot of the 5-minute interval (x-axis) and the 
    average number of steps taken, averaged across all days (y-axis)
    2. Which 5-minute interval, on average across all the days in the 
    dataset, contains the maximum number of steps?
"""
import csv
import statistics as st
import pygal
import matplotlib.pyplot as plt

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    dictDate = {}
    dictInterval = {}
    for row in reader:
        steps = row[0]
        if (steps != 'NA'):        
            date = row[1]
            interval = int(row[2])
            
            dictDate.setdefault(str(date),[])
            dictDate[str(date)].append(int(steps))  #adds steps per day
            
            dictInterval.setdefault(interval,[])
            dictInterval[interval].append(int(steps)) #adds steps per interval
    
    listDate = []
    listTotal = []
    
    for i in dictDate.keys():
        listDate.append(i)
        listTotal.append(sum(dictDate.get(i)))

    print("Mean: ",st.mean(listTotal))
    m = sorted(listTotal)
    print("Median: :",st.median(m))
    
    hist = pygal.Bar()
    hist.title = "Total steps taken per day"
    hist.x_title = "Steps per day"
    hist.x_labels = listDate
    hist.add("Total number of steps",listTotal)
    hist.render_to_file('ActivityTuesday.svg')

    listAvePerInterval = []
    for i in dictInterval.keys():
        listAvePerInterval.append(i)
        listAvePerInterval.append(sum(dictInterval.get(i)))
    
    plt.plot(list(dictInterval.keys()), listAvePerInterval, c="red")
    plt.title("Average Daily Activity")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken")
    plt.show()