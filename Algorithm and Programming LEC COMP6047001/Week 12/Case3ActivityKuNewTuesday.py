#%%
'''
CASE 3
Inputting missing values
1. Calculate and report the total number of missing values in the 
    dataset (i.e. the total number of rows with NAs)
2. Devise a strategy for filling in all of the missing values in the dataset
3. Create a new dataset that is equal to the original dataset but with 
    the missing data filled in.
4. Make a histogram of the total number of steps taken each day and 
    Calculate and report the mean and median total number of steps taken per day.
'''
#%%
import csv
import statistics as st
import pygal

filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headerRow = next(reader)
    
    wr = open('newActivity.csv','w')
    wr.write(str(headerRow[0])+","+str(headerRow[1]+","+str(headerRow[2])))
    wr.write("\n")
    
    n=0
    for row in reader:
        if(row[0] == 'NA'):
            row[0] = 0
            n+=1
        wr.write(str(row[0])+","+str(row[1])+","+str(row[2]))
        wr.write("\n")
        
    wr.close()
    print("The total number of missing values in the dataset is:",n)
    
filename = 'newActivity.csv'
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
    hist.render_to_file('NewActivityTuesday.svg')
#%%