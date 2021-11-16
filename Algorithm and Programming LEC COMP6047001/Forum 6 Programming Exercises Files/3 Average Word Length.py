"""
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths of the word tokens in the text, divided by the number of word tokens). [open http://www.gutenberg.org/ and download an e-book as plain text, use the file for texting your program]
"""
import os                                           #importing library to open file in specific location
os.chdir("c:/Users/Owen/Documents/GitHub/BINUSAssignment/Algorithm and Programming LEC COMP6047001/Forum 6 Programming Exercises (Files)")                     #specifying location of file

openFile = open("Test1.txt", "r")                   #opening first text file
readFile = openFile.read()                          #reading each line as a list
lenFile = len(readFile)                             #declaring the length of the read file
splitFile = readFile.split()                        #spliting the read file into list

sumLenWorTok = 0                                    #initial number of sum of lengths of word tokens in the text
numWorTok = 0                                       #inital number of number of word tokens

for word in splitFile:                              #for every word that has been splitted
    numWorTok += 1                                  #number of word tokens adds by 1 every word
    sumLenWorTok += lenFile                         #sum of lengths of word tokens times every word

aveWorLen = sumLenWorTok / numWorTok                #dividing sum of lengths of word tokens with number of word tokens to get average word length

print("The number of word tokens:", numWorTok)      #printing number of word tokens
print("The sum of all the lengths of the word tokens in the text:", sumLenWorTok) #printing sum of lengths of word tokens
print("The average word length of the text:", aveWorLen) #printing average word length