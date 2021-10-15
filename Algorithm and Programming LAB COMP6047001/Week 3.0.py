"""
# while loop
a = True

a = 0
while(a < 10):
    print("hello")
    a += 2

# for loop
li = [1, 2, 3, 4, 5]
for i in li:
    print(i)

for i in [1, 2, 3, 4, 5]:
    print(i)

range(5)
[0, 1, 2, 3, 4]
for i in [0, 1, 2, 3, 4]:
    print("i")

a = [1]
b = list(a)
b[0] = 21
print(a)
print(b)

li = [1, 2, 3, 4, 5]
print(li[1])
print(li[0:5])
"""
###
"""
I want you to accept a string input
output the same string, but in spongebob case

input   : ILIKECHOCOLATE
output  : iLiKeChOcOlAtE

input   : well done steak
output  : WeLl DoNe StEaK
"""
strings = input("Input your text: ")

var = ""
for i in range(len(strings)):
    if i % 2 == 0:
        var += strings[i].upper()
    else:
        var += strings[i].lower()
print(var)

#Kenneth
input1 = input("please enter your words to be spongebobcified")
counter = True
for i in input1:
    if counter:
        print(i.upper(), end = '')
    else:
        print(i.lower(), end = '')
    counter = not counter

#Arvin
isCapital = True
stringInput = (input("Input a string : "))
print(stringInput)
newString = ""

print("looping..")
for i in stringInput:

     if(isCapital == True):
          newString += i.upper()
     elif(isCapital == False):
          newString += i.lower()
     isCapital = not isCapital

print(newString)
