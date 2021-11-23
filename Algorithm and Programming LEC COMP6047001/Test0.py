import os
os.chdir("c:/Users/Owen/Documents/GitHub/BINUSAssignment/Algorithm and Programming LEC COMP6047001")
file = open("out.txt", "w")
s = "this"
print(s, "is a test", file=file)
file.close()