# first python script

# basic output
print('Hello again!')
print("This also works!")

# Careful with quotes when copy/pasting
# print(“Does this work?”)

print("I'm in class.") #to print a ' in output, enclose string in " "
print('He\'s also in class.') #use \' to print a ' in your string

print('I should finish watching "The Office" on Netflix. ') #to print a " in output, enclose string in ' '
print("I should also watch \"Cobra Kai\".") #use \" to print a " in your string

#python allows triple quotes! Great for multi-line strings
print('''There was an old man with a beard,
who said, "It is just as I feared!
Two Owls and a Hen,
Four Larks and a Wren,
have all built their nests in my beard!" ''')

print('Python is not so bad.\nI guess.') #\n new line escape character
print('Python is certainly different.')

#how to suppress the new line from print
print('3, ', end = ' ') #end = ' ' means to place a space after a string (using single quotes here)
print('2, ', end = ' ')
print('1. ')
print('3,', end = '') #end = '' means to place no spaces after a string (still using single quotes here)
print('2,', end = '')
print('1.')

#declaring variables
length = 10 #order is important

#identifier naming rules
'''
You can’t use reserved keywords as an identifier name.
Python identifier can contain letters in a small case (a-z), upper case (A-Z), digits (0-9), and underscore (_).
Identifier name can’t begin with a digit.
Python identifier can’t contain only digits.
Python identifier name can start with an underscore.
There is no limit on the length of the identifier name.
Python identifier names are case sensitive.
'''

#print (value in) length
print('The length is', length)

#to remove the space, use an item separator
print('The 2nd length is:', length, sep = '') #sep = '' says to remove spaces between string and value

# \ string continuation
print("The American child actor, Carl Switzer who played Alfalfa in The Little Rascals, \
is shot to death after allegedly attacking a man with a knife during an argument \
over $50. Switzer had been training a hunting dog for Moses Samuel Stiltz. When \
the dog escaped, Switzer paid a reward for his recovery and believed that Stiltz should \
reimburse him. When he confronted Stiltz about the reward money, a fight ensued and \
Stiltz shot and killed him.")

#use print() to create a skipped line
print()

monday = 250
tuesday = 325
wednesday = 400

#note: when \ is not part of the string, we can indent
print('On Monday we sold ', monday, 'units, ' \
            'on Tuesday we sold', tuesday, 'units, ' \
          'and on Wednesday we sold ', wednesday, 'units.')

print()

#string concatenation (adding strings together)
print("The American child actor, Carl Switzer who played Alfalfa in The Little Rascals," +
"is shot to death after allegedly attacking a man with a knife during an argument " +
"over $50. Switzer had been training a hunting dog for Moses Samuel Stiltz. When " +
"the dog escaped, Switzer paid a reward for his recovery and believed that Stiltz should " +
"reimburse him. When he confronted Stiltz about the reward money, a fight ensued and " +
"Stiltz shot and killed him.")

print()

#variable recap
length = 10 #length is int
print('length is', length)

#update length using mixed expression
length = length + 11.5 #length is now float
print('length is now', length)

#update length using string
length = 'too long for me to bother measuring.'
print('and length is now', length)

#create 'constant' (can't do it in Python, so make it clear)
MAX = 50

#input function return strings
name = input('Enter your name: ') #prompt - string
print('Hello ', name, '!', sep = '')

#input and convert to int() or float()
width = float(input('Enter width: '))
print('width is', width)

# // - int division
#% - remainder (after int division)
# ** - exponent

#operator precedence - note: ( ) override order
#1) **
#2) *   /   //   %
#3) + -

#multiple declaration
x, y = 1, 2
print('x is', x, 'y is', y)

#Test: prompt with print, use multiple inputs
print('\nEnter two values: ')
x, y = int(input()), int(input())
print('x is', x, 'y is', y)

#multiple assignment
y = x = 3
print('x is', x, 'y is', y)

#formatting
#1) string . format ( ) - high level
print('143/7 is', end = ' ')
print('{:.6f}'.format(143/7)) #{: } placeholder for the string
print('{:.4f}'.format(143/7))

print()
#2)low level format
print('143/7 is', format((143/7), '.6f' ))

#currencies - high level format
salary = 30000000
print('Ryan Kaji made $', '{:,.2f}'.format(salary), end = ' ')
print('in 2020.')

#currency - low level
print('Ryan Kaji made $', format(salary, ',.2f'), 'in 2020.', sep = ' ')

print()
#formatting percentages
print('{:%}'.format(0.5))
print('{:.1%}'.format(0.5)) #format with 1 decimal place
print('{:.0%}'.format(0.5)) #no decimal places

import math #used for getting predefined functions
#recommend - move imports and constants to the top of program
num = 12
num2 = math.pow(num, 2)
print(num2)

num = num + 1
num += 1 #compound assignments (will discuss more soon)
print (num)

#compound assignment operators
number = 10

#update
number = number  + 1 #number = 10 + 1 = 11
print(number)

#line 11 is equivalent to line 7
number += 1 #number = 11 + 1 = 12
print(number)

number -= 3 #number = 12 - 3 = 9
print(number)

number *= 1 #number = number * 1 = 9 * 1 = 9
print(number)

number /= 3 #number = number / 3 = 9 / 3 = 3.0 ( / - floating pt division)
print(number)

number //= 3 #number = number // 3 = 3.0 // 3 = 1.0 (due to mixed expression)
print(number)

another = 5
another //= 3 #another = 5 // 3 = 1
print (another)

number %= 4 #number = number % 4 = 1.0 % 4 = 1.0 (due to mixed expression)
print(number)

factor = 2
factor **= 3
print(factor)

#Note: be careful with more complex compound operations
var = 3
var += factor * 2 #var = var + (factor * 2)
print(var)

#reset var
var = 3
var = var + factor * 2
print(var)

var2 = 5
var2 = var2 * 6 + factor #var2 = 5 * 6 + 8 = 30 + 8 = 38
print(var2)

#reset var2
var2 = 5
var2 *= 6 + factor #var2 = var2 * (6 + factor) = 5 * (6 + 8) = 5 * 14 = 70
print(var2)

#selection using if
sales = float(input('Enter sales amount: '))

#if statement does not require () or { }
#use of () is fine for condition. For { } it must be part of the indentation
if sales > 50000:
    bonus = 500.0 #indentation is cruicial here. It indicates the beginning
    print('You get a bonus!') #and end of a block of statements associated with
    print('Your bonus is $', '{:.2f}'.format(bonus)) #the if statement.

print('This is not supposed to be in my if statement.') #and it isn't!

#transition to a while loop by changing the keywords!
#this is an infinite loop so be careful. use CTRL+ C to stop
'''while  sales > 50000:
    print('You get a bonus!')'''

score = float(input('Enter a score between 0 and 100: '))

#logical operator
#and - requires at least 2 expressions: require all conditions to be true for collective expression to be true
#or -  requires at least 2 expressions: require at least one condition to be true for collective expression to be true
#not - requires 1 expressions: inverts boolean expession

#input validation with an if statement - only works once
#if score < 0 or score > 100:
while score < 0 or score > 100: #work as needed
    score = float(input('Invalid score. Enter a score between 0 and 100: '))

#one way selection - if statement
'''if score >= 80:
    print ('You pass!')
    print ('Yes!')'''

#two way selection - if else statement (one outcome for true, and another for false)
if score >= 80:
    print ('You pass!')
    print ('Yes!')
else:
    print('Oh no!')
    print('Try again.')

#conditional expression is an alternative to if else
#Not recommended - may be hard to interpret and debug
print('You pass. Yes!' if score >= 80 else 'Oh no! Try again!')


#multiple selection - nested if else
if score >= 90:
    print('You pass. Grade is A')
else:
    if score >= 80:
        print('You pass. Grade is B')
    else:
        if score >= 70:
            print('Grade is C. Try again')
        else:
            if score >= 60:
                print('Grade is D. Try again')
            else: #trailing else
                print('Grade is F. Try again')

#multiple selection - if-elif-else
if score >= 90:
    print('You pass. Grade is A')
elif score >= 80:
    print('You pass. Grade is B')
elif score >= 70:
    print('Grade is C. Try again')
elif score >= 60:
    print('Grade is D. Try again')
else: #trailing else
    print('Grade is F. Try again')

#math operation have a higher order than relational and logical

# relational operator precedence
# 1) >  >=  <  <=
# 2) ==   !=

#logical operator precedence
# 1) not
# 2) and
# 3) or

name = 'Thompson'
print('The name', name, 'has', len(name), 'characters.') #use len() to get length of a string

#first position in a string is 0. Access a character using [ ].
print('\nThe first character in', name, 'is', name[0])

#you can use negative integers starting at -1 to read rightmost value
posn = -1
print('\nThe character at position', posn, 'in', name, 'is', name[posn])

name2 = 'McDaniels'
posn = -3
print('\nThe character at position', posn, 'in', name2, 'is', name2[posn])

#to slice a string (obtain a subset of it)
slname = name[0:5] #obtain all characters from 0 inclusive to 5 exclusive
print()
print(slname)

slname2 = name2[2:6] #obtain all characters from 2 inclusive to 6 exclusive
print()
print(slname2)


#strings are immutable (can't be changed)
#name[1] = 'C' #can't be done

#when name = 'Daniel' is done (legal), a new space in memory is allocated,
#lose access to 'Thompson' via variable called name
#Python will clean up (garbage collection)
#Memory leak vs Dangling pointer

#other immutable types: int, float, bool, tuple

#to 'add' new strings use +
str1 = 'Heck '
str2 = 'yeah'
print(str1 + str2)

#mutable: list, dict, sets
#list
nameList = ['Jack', 'Jake', 'Jane', 7]
print('\n', nameList)

#allowed to change a value at a specific position
nameList[3] = 'John'
print('\n', nameList)

mylist = [ ] #creates an empty list

#how to access a character from an element in a list
#nameList[1][2] - [1] refers to the element in the list,
#                 [2] refers to the character from the selected element
print(nameList[1][2])

#to create a 'nested' list
anotherList = [ nameList, 'Ringo', 'George', 'John', 'Paul']
print('\n', anotherList)

#list
names = ['Jack', 'Jake','Jane', 7] #lists can hold mixed types of data
print(names)

#lists are mutable: allowed to change value at a specific position
names[3] = 'John'
print('\n', names)

#You can put a list inside a list too!
moreNames = [names, 'Ringo', 'Homer']
print('\n', moreNames)

#You can access a character from an element in the list as well
#name [1] - get the element in that position;
#[0] gets the character in that position of the element!
print('\n', names[1][0])

#Since lists are mutable, you can use methods to add or remove elements
#methods are instructions for objects, and are executed by using dot operator with object.
names.append('Kyle')
print('\n', names)

names.pop(2) #removes value at postion 2 in list
print('\n', names)

names.remove('Jack') #removes specific value
print('\n', names)

#sequence type functions can operate on sequences like list or strings (no dot operator needed here)
print('\nThe length of the names list is', len(names))

#A tuple is like a list, but immutable
rates = (0.025, 0.01)
print(rates)

#can't do this: rates[0] = 0.25
#you can access a specific value in a tuple
print(rates[0])

#A set are unordered collection of unique elements. Two ways to create a set:
#1) use the set() function to create a set
ids = [1000, 1000, 1501, 1001, 1002, 1003, 1200, 1500, 1001]
idset = set(ids)
print(idset)

#2) use { } - set literal
newNames = {'Moses', 'Sarah', 'Abraham'} #set also allows mixed types
print('\n', newNames)

#sets are unordered so this won't work: (can't reference a specific position): newNames[2] = 'Peter'
#however sets are mutable (you can add or remove items using methods
newNames.add('Peter')
print('\n', newNames)

#dictionary is great for associative relationships
#needs key - immutable type
#value can be mutable
footballPlayers = {'Tom Brady': 12,
                   'Peyton Manning': 18}

print("\nTom Brady's jersey number is ", footballPlayers['Tom Brady'])

#When to use a list - if you have a collection of data that may need to be adjusted
#When to use a tuple - if you know data should not be changed
#When to use a set - if you want to collect unique items (and don't care about order)
#When to use a dict - if you want to store assocated data

#split function - to split a string into substrings (7.4)
fullname = 'FirstName MiddleName LastName'
print('\n', fullname.split())

#you can also specify which separator to use to split a string. default separator is whitespace
print('\n', 'FirstName,MiddleName,LastName'.split(','))

#split can be used for input as well. Since input function reads strings, it can be used fror multiple input
num1, num2 = input('Enter 2 values (separated by spaces): ').split()
print('num1 is', num1, 'and num2 is', num2)

#don't forget to convert for calculations
num1 = float(num1)
num2 = float(num2)
print(num1 - num2)

#while loop for counting
i = 1 #variable i represents loop control variable
while i <= 5:
    print(i)
    i = i + 1  #update statement (prevents loop from running infinitely)

#common operation - iterating over a container (such as a list). a for loop can be used here:
anotherList = ['Steve', 'Dwight', 'Phyllis', 'Jim', 'Pam']

for n in anotherList:
    print('Hello {}!'.format(n)) #{} is a replacement field for strings

#You can iterate over a string as well:
phrase = 'The Mucky Duck'
for j in phrase:
    print(j)

#you can use in (with logical operators) with if statements as well
if 'a' not in phrase:
    print("I didn't find 'a'!")
else:
    print("I found 'a'!")

#while loop (counting)
i = 1 #variable i - loop control variable - initialization
while i <= 15: #condition
    print(i, end =' ')
    i = i + 1 #update (prevent infinite loop)

print()

for j in range(15): #count from 0 to 14
    print(j, end = ' ')

print()

for k in range(20, 36): #count from 20 to 35 inclusive
    print(k, end = ' ')

print()

for k2 in range(-10, 0):
    print(k2, end = ' ')

print()

for m in range(100, 351, 50): #count from 100 to 300, incrementing by 50
    print(m, end = ' ')  #(add 1 to upper limit to include 350)

print()

for m2 in range(350, 99, -50): #count in reverse, decriment by 50
    print(m2, end = ' ')  #(subtract 1 from upper limit to include 100)

#example from previous lecture
#common operation - iterating over a container (such as a list) a for loop can be used here:
#7, 8, 9 is added to show that different types will be printed as well
anotherList = ['Steve', 'Dwight', 'Phyllis', 'Jim', 'Pam', 7, 8, 9]

#n is the loop control variable
for n in anotherList:
    #print('Hi {}!'.format(n)) #{} is a replacement field for strings
    #print('Hi', n) #lower level alternative
    print(f'{n}') #newer alternative to format

#iterating over a string
words = "Merry Christmas!"

for w in words:
    print(w, end = '...')

for v in range(100):
    if v > 15:
        break #break statement - interrupt the loop completely
    print(v, end = ', ')

print()

for v2 in range(10, 20):
    if v2 == 13:
        continue
    print(v2, end = ' - ')

#for else example
for i2 in range (1, 4):
    print(i2)
else: #runs because there was no interruption to loop
    print('No break in loop.')

#for else example
for i2 in range (1, 4):
    print(i2)
    break
else: #does not run because there was an interruption
    print('No break in loop.')

import random

#loop else structure
for i in range(1, 4):
    print(i)
else: #executed because the loop ran successfully
    print('No interruptions.')

print()

#loop else structure (with break)
for i in range(1, 4):
    print(i)
    break
else: #does not execute because the loop was affected by a break
    print('No interruptions.')

print()

#loop else structure (with continue)
for i in range(1, 8):
    if i == 5:
        continue
    print(i)
else: #executed because the loop ran successfully (even with skips)
    print('No interruptions.')

#nested loops
#for every 1 iteration of the outer loop, inner loop complete ALL iterations
#to determine total number of iterations:
#calculate number of iterations for each loop, then multiply
digit1 = 0
digit2 = 0
while digit1 <= 9: #outer loop
    digit2 = 0
    while digit2 <= 9: #inner loop
        print('{} -- {}'.format(digit1, digit2)) #freplacement field { } used to print 'pattern'
        digit2 += 1
    digit1 += 1

#fun with RNG
for x in range(10):
    number = random.randrange(20) #generate ints from 0 to 19
    print(number)

print()

for x in range(10):
    number = random.randrange(1, 100) #generate ints from 1 to 99 (100 is exclusive)
    print(number)

print()

#randint will include both limits
for x in range(10):
    number = random.randint(1,100) #generate ints from 1 to 100
    print(number)

print()
for x in range(10):
    number = random.randrange(1, 101, 5) #generates ints from 1 to 100 in steps of 5
    print(number)

print()
for x in range(10):
    print(random.random()) #generate a floating point between [0, 1)

print()
for x in range(10):
    print(random.uniform(3.0, 8.0)) #generate a floating point between 3 and 8 (8 is inclusive because of rounding)

print()
#use random.choice for sequences
for x in range(10):
    print(random.choice(['heads', 'tails']))
