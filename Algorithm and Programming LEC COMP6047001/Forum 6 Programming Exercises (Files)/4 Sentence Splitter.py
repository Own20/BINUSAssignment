"""
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence splitting includes (but isn't limited to) the following rules:
    Sentence boundaries occur at one of "." (periods), "?" or "!", except that .
    Periods followed by whitespace followed by a lower case letter are not sentence boundaries.
        a) Periods followed by a digit with no intervening whitespace are not sentence boundaries.
        b) Periods followed by whitespace and then an upper case letter, but preceded by any of short list of titles are not sentence boundaries.
        c) Sample titles include Mr., Mrs., Dr., and so on.
        d) Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries
        e) (for example, www.aptex.com, or e.g).
        f) Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file can write its content with each sentence on a separate line. Test your program with the following short text:

Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a probability of .9 it isn't.

The result should be:

Mr. Miyagi bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it.
Did he mind?
Adam Jones Jr. thinks he didn't.
In any case, this isn't true...
Well, with a probability of .9 it isn't.
"""
import os                                           #importing library to open file in specific location
os.chdir("c:/Users/Owen/Documents/GitHub/BINUSAssignment/Algorithm and Programming LEC COMP6047001/Forum 6 Programming Exercises (Files)")                     #specifying location of file

newFile = open("4 Text.txt", "w")                   #opening new file to be written

inpText = input("Enter text:")                      #inputing text

if "Mr." in inpText:                                #if Mr. is in the inputed text
    repText = inpText.replace("Mr.", "Mister")      #replacing Mr. with Mister
if "Mrs." in repText:                               #if Mrs. is in the inputed text
    repText = repText.replace("Mrs.", "Missus")     #replacing Mrs. with Missus
if "Dr." in repText:                                #if Dr. is in the inputed text
    repText = repText.replace("Dr.", "Doctor")      #replacing Dr. with Doctor
if "Jr." in repText:                                #if Jr. is in the inputed text
    repText = repText.replace("Jr.", "Junior")      #replacing Jr. with Junior
if "i.e." in repText:                               #if i.e. is in the inputed text
    repText = repText.replace("i.e.", "ie")         #replacing i.e. with ie
if "e.g." in repText:                               #if e.g. is in the inputed text
    repText = repText.replace("e.g.", "eg")         #replacing e.g. with eg

lineText = repText.replace(". ", ".\n")             #replacing period with a period and enter
line1Text = lineText.replace("? ", "?\n")           #replacing question mark with a question mark and enter
line2Text = line1Text.replace("! ", "!\n")          #replacing exclamation mark with an exclamation mark and enter

if "Mister" in line2Text:                           #if Mister is in the new text
    newText = line2Text.replace("Mister", "Mr.")    #replacing Mister with Mr.
if "Missus" in newText:                             #if Missus is in the new text
    newText = newText.replace("Missus", "Mrs.")     #replacing Missus with Mrs.
if "Doctor" in newText:                             #if Doctor is in the new text
    newText = newText.replace("Doctor", "Dr.")      #replacing Doctor with Dr.
if "Junior" in newText:                             #if Junior is in the new text
    newText = newText.replace("Junior", "Jr.")      #replacing Junior with Jr.
if "ie" in newText:                                 #if ie is in the new text
    newText = newText.replace("ie", "i.e.")         #replacing ie with i.e.
if "eg" in newText:                                 #if eg is in the new text
    newText = newText.replace("eg", "e.g.")         #replacing eg with e.g,

print(newText)                                      #printing new text
newFile.write(newText)                              #printing nex text to new file

newFile.close()                                     #closing new file