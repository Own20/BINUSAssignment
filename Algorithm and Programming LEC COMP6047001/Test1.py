import os
os.chdir("c:/Users/Owen/Documents/GitHub/BINUSAssignment/Algorithm and Programming LEC COMP6047001")

import string

f = open("test1.txt", "r")
txt = f.read(). lower().replace("\n", "")
newTxt = ""
for c in txt:
    if c not in string.punctuation:
        newTxt += c
txt = newTxt
lst = txt.split(" ")
d = {}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
newd = []
for i in d:
    if d[i] == 1:
        newd.append(i)
print("These are the hapaxes found in the text: ")
for word in newd:
    print(word)