#%%
from datetime import datetime

fDate = datetime.strptime('2021-7-1','%Y-%m-%d')
print(fDate)
#%%
import csv
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    headRow = next(reader)
    print(headRow)
    
    for i, colHead in enumerate(headRow):
        print(i,colHead)

#extract high temperatures from the file
    dates, highs = [], []
    for row in reader:
        cDate = datetime.strptime(row[0],'%Y-%m-%d')
        dates.append(cDate)
        
        high = int(row[1])
        highs.append(high)

#get average high temperature from the file
    averageHighTemp = sum(highs)/len(highs)
    print(averageHighTemp)

#plotting the high temperatures
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red')
fig.autofmt_xdate()
plt.title("Daily High Temperatures",fontsize=15)
plt.xlabel('',fontsize=10)
plt.ylabel('Temperature (F)',fontsize=10)
plt.show()

#%%
