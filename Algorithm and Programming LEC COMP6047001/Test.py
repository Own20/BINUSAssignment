"""
Write a program that counts the number of times a word occured in a sentence.
    1. Read input from the user
    2. Create a function that accepts the input and thereafter returns a dictionary containing the word count and the word

Example:
    Enter a sentence: i am who i am
    2 i
    2 am
    1 who
"""
def countWords(myStr):                              #i am who i am
    myDict = {}
    splitWords = myStr.split()                      #['i', 'am', 'who', 'i', 'am']
    for word in splitWords:
        myDict[word] = myDict.get(word, 0) + 1
        #myDict[i] = 1
        #myDict[am] = 1
        #myDict[who] = 1
        #myDict[i] = 1
        #myDict[am] = 1
    #myDict = {'i': 2, 'am': 2, 'who': 1}
    return myDict

myStr = input("Enter a sentence: ")

myWordCount = countWords(myStr)
for key in myWordCount:
    print(myWordCount[key], key)