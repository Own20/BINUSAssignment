"""
Write a program that given a text file will create a new text file in which all the lines from the original file are numbered from 1 to n (where n is the number of lines in the file).
"""
import os                                                   #importing library to open file in specific location
os.chdir("c:/Users/Owen/Documents/GitHub/BINUSAssignment/Algorithm and Programming LEC COMP6047001/Forum 6 Programming Exercises (Files)")                             #specifying location of file

openFile = open("Test1.txt", "r")                           #opening first text file
readFile = openFile.readlines()                             #reading each line as a list

newFile = open("2 Text.txt", "w")                           #createing new text file

num = 1                                                     #starting the line numbering
for lines in readFile:                                      #for every lines in the file
    newFile.write("(" + str(num) + ")" + " " + lines)       #printing numbers and lines
    num += 1                                                #numbers add 1 every new line

openFile.close()                                            #closeing first text file
newFile.close()                                             #closeing new text file