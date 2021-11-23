"""
Files
1. Read and Write to files (txt files)
    a. Reading files - 
        open("", "r"),
        read(),
        close(),
        tell(),
        seek(),
        read and readline() - returns a string
        readlines() - returns a list
    b. writing to files
        open("filename", "w")
        write() - arg is string,
        writelines() - arg is either list / tuple
"""
import os
os.getcwd() #where files stored

#specify the path where you like to open the file
os.chdir("c:/Users/Owen/Documents/GitHub/BINUSAssignment/Algorithm and Programming LEC COMP6047001")
# #location of the text file if different location specify, if the same no need

# ls *.txt #search text file

myFile = open("Test1.txt", "r")
# type(myFile)
fileContents = myFile.read()                                  #returns a string
print("FileContents:", fileContents, " ", len(fileContents))  #already read until the end of file (EOF) <- file pointer
# print("FileContents:", fileContents, " ", myFile.tell())
# fileContents = myFile.read()
# print()
# myFile.close() #after close then you can access it again
# myFile = open("test.txt", "r")
# fileContents2 = myFile.read()
# print("FileContents2:", fileContents2, " ", len(fileContents2))
# print("FileContents2:", fileContents2, " ", myFile.tell())

# myFile = open("test.txt", "r")
# line1 = myFile.readline() #returns a string
# line2 = myFile.readline()
# print(line1)
# print(line2)
# lines = myFile.readlines() #returns a list

# for line in lines:
#     print(line, sep="", end="")

# #treat the file as an iterable
# for line in lines:
#     print(line, sep="", end="") #not list or string only accessing the file

# outputFile = open("info.txt", "w")
# a = 1.0
# b = "this"
# c = [13, 4.5]
# d = {1, 2, 3, 4, 5}
# outputFile.write("{} {} {} {}\n". format(a, b, c))
# print(a, b, c, d, file=outputFile)
# outputFile.close()

# out1 = open("out1.txt", "w")
# out2 = open("out2.txt", "w")
# v1 = ["one", "two", "three"]
# v2 = ("one\n", "two\n", "three\n")
# out1.writelines(v1)
# out2.writelines(v2)
# out1.close()
# out2.close()