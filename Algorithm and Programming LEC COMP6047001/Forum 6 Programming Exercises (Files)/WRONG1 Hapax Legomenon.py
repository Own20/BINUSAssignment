"""
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a language, the works of an author, or in a single text.
Define a function that given the file name of a text will return all its hapaxes. Make sure your program ignores capitalization.
[open http://www.gutenberg.org/ and download an e-book as plain text, use the file for texting your program]

1. lower case
2. remove punctuation
3. make list
4. scan everything with loop
5. identify hapax
"""
import os
import string

os.chdir("c:/Users/Owen/Documents/GitHub/BINUSAssignment/Algorithm and Programming LEC COMP6047001")


def hapax():
    file = open("test1.txt", "r")
    fileStr = file.read()
    fileRep = fileStr.replace("\n", "")
    fileLow = fileRep.lower()

    noPunc = ""
    for word in fileLow:
        if word not in string.punctuation:
            noPunc += word

    fileDone = fileStr.split()

    d = {}
    for i in fileDone:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    fileContents = list(fileDone)
    for i in d:
        if d[i] == 1:
            fileContents.append(i)

    for words in fileContents:
        print(words)

print(hapax())