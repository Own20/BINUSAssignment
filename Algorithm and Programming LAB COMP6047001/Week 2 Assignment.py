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