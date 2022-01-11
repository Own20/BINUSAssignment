#%%
'''

Create a python script that would be able to display the information being 
asked for:
    CASE 1
    What is mean total number of steps taken per day?
    For this part of the task, we ignore the missing values (NA) in the dataset.
    1. Calculate the total number of steps taken per day
    2. Make a histogram of the total number of steps taken each day
    3. Calculate and report the mean and median of the total 
        number of steps taken per day
    
    CASE 2
    What is the average daily activity pattern?
    1. Make a time series plot of the 5-minute interval (x-axis) and the 
    average number of steps taken, averaged across all days (y-axis)
    2. Which 5-minute interval, on average across all the days in the 
    dataset, contains the maximum number of steps?
'''
#%%
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
        listAvePerInterval.append(st.mean(dictInterval.get(i)))
    
    plt.plot(list(dictInterval.keys()),listAvePerInterval,c='blue')
    plt.title("Average Daily Activity")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken")
    plt.show()
    
    maxValue = max(listAvePerInterval)
    n = 0
    max = ""
    indexMax = listAvePerInterval.index(maxValue)
    
    for i in dictInterval.keys():
        if (n==indexMax):
            max = i
            break
        n+=1
        
    print("maximum number of steps in interval: " +str(max))
#%%