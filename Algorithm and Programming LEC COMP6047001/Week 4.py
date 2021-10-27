"""
1. range()
    syntax: range([start],stop, [increment])
2. Mutability (list), Immutability (Strings an
3. for loops within for loops (nested loops)
4. list of lists
    a. Indexing embedded lists common between string, list , tuple indexing
5. References and list mutability
6. Strings as iterables or sequences
7. Negative indices
8. Slicing
    x[[start] : [stop] ]
    x[[start] : [stop] : [increment]]
9. string functions
    lower(),upper(),capitalize(),title(), swapcase(), count(), strip(), lstrip(),
    rstrip(), find(), index(), replace(), split(), join()

[] -> list
() -> tuple
"", '' -> string
{} -> dictionary
"""
# x = [1, 2, 3, 4]
# print(type(x))

# x[0] = 10
# # x = [10, 2, 3, 4]

# x[-1]

# for i in range(7): # loops from 0 to 6
#     for j in range(1, i + 2):
#         print(j, end="")
#     print()

# for i in range(3):
#     for j in range(5):
#         print("i=", i, "j=", j)

#basic
# for i in range(7):
#     for j in range(1, i + 2):
#         print("#", end="")
#     print()

#python
# for i in range(7, 0):
#     print("#" * (i - 1))

# for i in range(7):
#     print("#" * (7 - i))

# for i in range(7):
#     print("#" * (7 - i), end="")
#     for j in range(1, i + 2):
#         print(j, end="")
#     print()

# for i in range(7):
#     print(" " * (7 - i), end="")
#     for j in range(1, i + 2):
#         print(j, end="")
#     for k in range(i, 0, -1):
#         print(k, end="")
#     print()

# xlist = [1, 2, 3]
# ylist = xlist #aliasing -> ylist is an alias of xlist
# xlist[0] = 35
# print(xlist, ylist)
# ylist[1] = 35
# print(xlist, ylist)
# ylist = []

# xlist = [1, 2, 3]
# ylist = xlist
# print(ylist is xlist)
# ylist[]
# print(ylist is xlist)

# xlist = [1, 2, 3]
# ylist = xlist
# print(ylist is xlist)
# ylist = xlist.copy()
# print(ylist is xlist)
# print(ylist)

# myStr = "Binus International"
# myStr[::-1] #reverse
# myStr[-1:len(myStr)-1:-1] #reverse

"""
functions
syntax: def <functionName> (<parameterlist>):
            <body>
1. void functions
2. non-void functions
"""
#declaration / definition
# def sayHi():
#     print("Hello")
#     print("My first user defined function")

# def greetUser(name):
#     sayHi()
#     print("Oops, you are", name)

# def getAge(age):    #non-void function
#     return age + 10
# #invocation
# # greetUser("Alysha")
# myName = input("Enter name: ")
# greetUser(myName)
# # print(type(greetUser("a")))
# myAge = int(input("Enter age: "))
# myNewAge = getAge(myAge)
# print(myNewAge)

#import functino from another file
#from myFunctions import *
#greetUser("Vincent")
#print("Your age: ", getAge(40))

"""
Create a function that accepts a parameter the number of lines to display in Pascals Triangle
"""
def generatePascalTriangle(numLines):
    for i in range(numLines):
        print(" " * (numLines - i), end="")
        for j in range(1, i + 2):
            print(j, end="")
        for k in range(i, 0, -1):
            print(k, end="")
        print()

# num = int(input("Enter number of lines: "))
# generatePascalTriangle(num)

"""
Function that returns the square of a number
"""
def square(num):
    return num*num

def main():
    num = int(input("Enter number of lines: "))
    generatePascalTriangle(num)

    s = square(num)
    print(s)

main()