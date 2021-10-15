#%%
n = 10
while n >= 0:
    if n == 5:
        pass
    else:
        print(n,"...",sep=" ")
    n = n-1
print("Blast off")
#%%
n = 10
while True:
    print(n,"...",sep=" ")
    n = n - 1
    if n == -1:
        break
print("Blast off")
#%%
x = 0.0
while x <= 1.0:
    print(x)
    x += 0.1
#%%
age = 0
while age <= 0:
    age = eval(input("Enter age [>0]:"))
print("You are",age,"years old")

#%%
lcv = 1         #loop control variable
while lcv <= 10:#conditon (repeat the body as long as condition is True)
    print(lcv)  #body
    lcv += 1    #change of state
print("Done")
#%%
'''
Topic for Today:
    1. while loop
        syntax:
            while <test_expr> :
                <body>
        finite and infinite loops, break, continue, pass
    2. Lists (mutable)  ---> []
        Creating a list 
        Indexing
        Length of a list [len()]
        Assignment
        Some useful functions : append(),extend(),insert(index,val),
                                remove(value or index),
                                min(),max(),sum(),sort()
                                islower(),isupper() - strings functions
    3. for loop
        syntax:
            for <item> in <iterable>:
                <body>
    4. range([start] default = 0,stop(exclusive),[increment] (default +1))        
'''
#%%

#%%
# code that appends items in the list via user input
myList = []
while True:
    myData = input("Enter value: <press return to stop>")
    if not myData: #myData == ""
        break
    else:
        myList.append(myData)
        continue
print(myList)
# code that removes an item from the list
val2Remove = input("Enter value to remove from the list >>")
for item in myList:
    if item == val2Remove:     
        myList.remove(item)
print(myList)
#%%
daysOfWk = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in daysOfWk:
    print(day)
#%%
numDay = 0
daysOfWk = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
for day in daysOfWk:
    numDay += 1
    print(numDay,day)











#%%