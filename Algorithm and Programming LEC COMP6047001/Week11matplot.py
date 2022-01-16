#%%
import matplotlib.pyplot as plt

#xValues = list(range(1,1001))  #1..1000
#yValues = [x**2 for x in xValues] #1**2....1000**2

xValues = [1,2,3,4,5]
yValues = [1,4,9,16,25]

plt.scatter(xValues, yValues)
plt.title("Square numbers",fontsize=20)
plt.xlabel("Value",fontsize=10)
plt.ylabel("Square of Value",fontsize=10)
plt.tick_params(axis='both',labelsize=10)
plt.show()
#%%
import matplotlib.pyplot as plt

xValues = list(range(1,1001))  #1..1000
yValues = [x**2 for x in xValues] #1**2....1000**2

plt.plot(xValues, yValues)
plt.title("Square numbers",fontsize=20)
plt.xlabel("Value",fontsize=10)
plt.ylabel("Square of Value",fontsize=10)
plt.tick_params(axis='both',labelsize=10)
plt.savefig('mySquares.png')
plt.show()
#%%