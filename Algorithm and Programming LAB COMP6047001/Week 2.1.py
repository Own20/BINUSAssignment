"""
and, or, not
true, false (boolean)

if(condition):
    stuff
elif(condition2):
    stuff
elif(condition3):
    stuff
else:
    last
"""
###
"""
a = 3
b = 5

print (a > b) #boolean value = true / false

if(a > b):
    print(a)
else:
    print(b)

if(a > b):
    print(a)
elif(a == b):
    print("same")
else:
    print(b)
"""
###
"""
- inputs a score

if score is 100, output A+
if score is 90 - 99, output A
if score is 80 - 89, output B
if score is 70 - 79, output C
if score is 60 - 69, output D
if score is 50 - 59, output E
below 50 is F

score = int(input("Enter score: "))
if score == 100:
    print("A+")
elif score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
elif score > 50:
    print("E")
else:
    print("F")
"""
###
"""
input a single non capital letter
output vowel/consonant (aeiou)/(everything else)

letter = input("Enter letter:")
if(letter == "a" == "e" == "i" == "u" == "o"):
    print("vowel")
else:
    print("consonant")
"""
###
"""
input an integer value

if it's divisible by 11, print a
if it's divisible by 9, print b
if it's divisible by 7, print c
if it's divisible by 2, print d
everything else print e

example cases
input: 63
output: bc
input: 22
output: ad

put it on your github repository
"""
integer = int(input("Enter integer:"))
a = integer % 11 == 0
b = integer % 9 == 0
c = integer % 7 == 0
d = integer % 2 == 0
if(a and b):
    print("ab")
elif(a and c):
    print("ac")
elif(a and d):
    print("ad")
elif(b and c):
    print("bc")
elif(b and d):
    print("bd")
elif(c and d):
    print("cd")
elif(a):
    print("a")
elif(b):
    print("b")
elif(c):
    print("c")
elif(d):
    print("d")
else:
    print("e")