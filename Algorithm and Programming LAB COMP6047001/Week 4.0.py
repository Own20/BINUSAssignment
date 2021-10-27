# for i in range(5):        #0, 1, 2, 3, 4
#     for j in range(10):   #(0, 1, ..., 9)
#         print("The value of i is: ", i)
#         print("The value of j is: ", j)
#     print("j done")

# for i in range(3):          #(0, 1, 2)
#     variable = i            #variable = 0
#     while(variable < 10):   #false
#         variable += 4
#     print(variable)

"""
I want you to print out a chessboard
You have a list of [A, B, C, D, E, F, G, H] and [1, 2, 3, 4, 5, 6, 7, 8]

A8B8C8D8E8F8G8H8
A7B7C7D7E7F7G7H7
A6B6C6D6E6F6G6H6
A5B5C5D5E5F5G5H5
A4B4C4D4E4F4G4H4
A3B3C3D3E3F3G3H3
A2B2C2D2E2F2G2H2
A1B1C1D1E1F1G1H1
"""
# col = ["A", "B", "C", "D", "E", "F", "G", "H"]
# row = ["1", "2", "3", "4", "5", "6", "7", "8"]

# print(col[0] + row[7], end="")
# print(col[1] + row[7], end="")
# print(col[2] + row[7], end="")
# print(col[3] + row[7], end="")
# print(col[4] + row[7], end="")
# print(col[5] + row[7], end="")
# print(col[6] + row[7], end="")
# print(col[7] + row[7], end="")

# for i in range(8):
#     for j in range(8):
#         print(col[j] + row[7 - i], end=" ")
#     print()
"""
Create a list
[
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8"]
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8"]
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"]
    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]
    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8"]
    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"]
    ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"]
    ["H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8"]
]
li = []
li.append([])
li[0].append(chr(65) + str(1))
li[0].append(chr(65) + str(2))
li[0].append(chr(65) + str(3))
li[0].append(chr(65) + str(4))
li[0].append(chr(65) + str(5))
li[0].append(chr(65) + str(6))
li[0].append(chr(65) + str(7))
li[0].append(chr(65) + str(8))
"""
# li = []
# for i in range(8):
#     li.append([])
#     for j in range(8):
#         li[i].append(chr(65 + i) + str(j + 1))
# print(li)

# row = int(input("Input how many rows you want: "))
# col = int(input("Input how many column you want: "))
# li = []
# for i in range(row):
#     li.append([])
#     for j in range(col):
#         li[i].append(chr(65 + i) + str(j + 1))
# print(li)

# li = []
# li2 = []
# for i in range(8):
#     for j in range(8):
#         li2.append(chr(65+j) + str(8-i))
#     li.append(li2)
# for i in range(len(li)):
#     print(li[i])

# li = []
# for i in range(8):
#     li.append([])
#     for j in range(8):
#         li[i].append(chr(65 + i) + str(j + i))

# for i in range(8):
#     for j in range(8):
#         print(li[j][7 - i], end=" ")
#     print("")

# for i in range(8):
#     for j in range(8):
#         print(li[j][i], end ="")
#     print("")

"""
I want a program that takes an integer from the user and then the program will print out "hello world" by the same amount of time as the user input

After that, the program will take another integer from the user and then will print out "hi" by the same amount of time as the user input

And then go back to hello world, until the user inputs -999

Input1: 5
Output:
hello world
hello world
hello world
hello world
hello world

Input2: 3
hi
hi
hi
"""
# while True:
#     inp1 = int(input("Enter number1: "))
#     if inp1 == -999:
#         break
#     for i in range(inp1):
#         print("hello world")
    
#     inp1 = int(input("Enter number2: "))
#     if inp1 == -999:
#         break
#     for i in range(inp1):
#         print("hi")

inp = 0
while inp != -999:
    inp = int(input("Enter number1: "))
    if inp != -999:
        break
    for i in range(inp):
        print("hello world")
    inp = int(input("Enter number2: "))
    for j in range(inp):
        print("hi")
    inp = int(input("Enter number3: "))