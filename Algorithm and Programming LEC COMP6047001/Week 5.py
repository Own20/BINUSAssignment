"""
Functions
0. User defined and Pre-defined
1. Declaration
    def <functionName> ([<parameters>]):
        <body>
2. Invocation
3. Important concepts:
    #local - refers to an identifier defined within a function or block
    #scope of local identifiers - can be used from point of declaration to end of the block

    #global - refers to an identifier defined outside a function or block
    #scope of global identifiers - can be used in any function or block as long as there isn't a local variable with the same name
4. Void and non-void functions
5. Parameters and parameter passing (by value, by reference)
"""
# #declaration (place to create function)
# #mutator or setter functions
# def greetings():    #void funtion, no parameters
#     print("Hello")
#     print("Goodbye")

# def greetMe(name):  #void function, with 1 parameter
#     print("Hello", name)

# def addMe(x,y):
#     sum = x + y
#     print("Sum of", x, "and", y, "is", sum)

# def myPow(base, exp):
#     return base ** exp

# #invocation (place to execute function)
# greetings()
# print("End")
# greetMe("Tartaglia")
# myStr = "Childe"
# greetMe(myStr)
# addMe(2, 4.5)
# a = 5
# b = 10
# addMe(a, b)
# x = 2
# y = 4
# addMe(x, y)

# w = addMe(x, y)
# print(w)

# v = myPow(2, 3)
# print(v)
# print(myPow(3, 3))
# #if there is a return, we need a variable to store it

# #main() function - used as a driver

# w = print("Hi") #Hi
# print(w)        #None
# type(w)         #NoneType
"""
Create a function called divmod that accepts 2 parameters x and y and returns the quotient and remainder of x and y
"""
# def divMod(x, y):
#     # q = x // y
#     # r = x % y
#     # return q, r
#     return x//y, x%y
# a, b = divMod(10, 5)
# print(a, b)

# n1 = int(input("Enter first digit : "))
# n2 = int(input("Enter second digit :"))
# def divmod(x, y):
#   return {f'quotient:{x//y} , remainder: {x%y}'}
# print(divmod(n1,n2))

###

# def getWtHt():
#     weight = float(input("Enter weight in kg: "))
#     height = float(input("Enter height in cm: "))
#     return weight, height
# weight, height = getWtHt()
# print(weight, ",", height)

# weight = 160                           #global
# def changeWt(weight):                  #local, pass by value
#     #whatever gets in, does not gets out
#     weight = weight - 10
#     print("weight is now ", weight)
# print(changeWt(weight))
# print(weight)

# weight = 160
# #getter or accessor functions
# def changeWt(weight):
#     return weight - 10
# weight = changeWt(weight)
# print(weight)

# def f0(x):
#     def g0(y):
#         return y ** 3 + 3
#     return g0(x) ** 4 + 4
# f0(4)
# g0(4)

# print("Hi")
# print("bye", end="")
# print("bye", end1="") #error
# print("Oi", "Ai", sep="#")
# print("bye", "hi", end="", sep="#")
# print("bye", "hi", sep="", end="#")

# def square(x):
#     return x * x
# square(10)
# square(x = 10)
# # square(y = 10) #error
# y = 5
# square(y)
# square(y = 3) #error
# square(x = y)

# def myPow (base, exponent = 2):
#     return base ** exponent
# myPow(10)       #base = 10, exponent = 2
# myPow(3, 0.5)   #base = 3, exponent = 0.5
# myPow(base = 3) #base = 3, exponent = 2

# def myPow (base = 3, exponent = 2):
#     return base ** exponent
# myPow()             #base = 3, exponent = 2
# myPow(exponent = 4) #base = 3, exponent = 4
# myPow(exponent = 5, base = 10)

# import math
# num = 34.45678
# round(num, 2)