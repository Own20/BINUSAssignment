'''
Control structures
1. Sequential -> one line program after the other
2. Conditional (boolean - True or False)    -> certain condition program
3. Repetitive

Basic Input/Output (I/0) (print(), input())
Explicit Type conversion - str(), int(), float()
#certain data type force to become other data type
Inplicit type conversion
#certain data type changes with the program
eval() - used to evaluate strings
chr(<int>)
ord(<char>)
Comparison operators
<,>,<=,>=,==,!=
Logical operators
and - if both are true, the result it true 
or  - if at least one is true, the result is true
not - not true is false, not true is false

if <test_expression>:   #true or false
    <body>

if <test_expression>:
    <body1>
else:
    <body2>

if <test_expression>:
    <body1>
elif <test_expression2>:
    <body2>
...
elif <test_expression>:
    <bodyn>
else:
    <bodynn>
'''
#%%
#name = input("Enter your name: ")       #input -> string
#print ("Hi",name)
#age = int(input("Enter your age: "))    #change the type of input
#print ("You old",age)

#value = '5 + 12'
#print (eval(value))
#print (type(value))
#value = eval (value)
#print (type(value))

#if True:
#    print ("Hi there")

#bt = True
#if bt:
#    print ("Hi there")
#print (type(bt))

#if 6*3-18:
#    print("is this ok?")
#if 6*3-19:
#    print("is this ok?")
#if 1+1 > 1:
#    print("is this ok?")

#x = 0.1
#bt = 1 == 10*x
#print (bt)

#grade = 90
#if grade > 80:
#    print("Good job")
#    print("Nice")
#else:
#    print("No good")
#    x = 10
#    y = 50
#    print(x,y)
#print("Print anyway!")

#grade = int(input("Enter mark:"))
#if grade >= 90:
#    print("A")
#elif grade >= 80:
#    print("B")
#elif grade >= 70:
#    print("C")
#elif grade >= 60:
#    print("D")
#elif grade >= 50:
#    print("F")
#else:
#    print("F")
#print("DONE!")

#grade = int(input("Enter mark:"))
#if grade >= 90 and <= 100:
#    print("A")
#elif grade >= 80 and < 90:
#    print("B")
#elif grade >= 70 and < 80:
#    print("C")
#elif 70 >= grade > 60:
#    print("D")
#elif 60 > grade >= 50:
#    print("F")
#else:
#    print("F")
#print("DONE!")