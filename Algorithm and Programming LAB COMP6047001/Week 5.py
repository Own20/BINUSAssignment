# def main():
#     print("Hello world")

# if __name__ == "__main__":
#     main()

# def call_hello():
#     print("hello world")
#     print("hi")
#     print("ok")
# call_hello()
# call_hello()

# def call_hello(x, y, z):
#     print(x)
#     print(y)
#     print(z)
# call_hello(1, 2, 3)
# call_hello(y = 1, x = 2, z = 3)

# def calcul(x):
#     return x ** 2 / 3 + 5
# print(calcul(5))
# print(5 ** 2 / 3 + 5)

# def calcul(x):
#     x ** 2 / 3 + 5
# print(calcul(5))

# def addx(x):
#     #global x
#     x += 1
#     print(x)
#     #print(id(x))
# x = 5
# print(x)
# addx(x)
# print(x)
# #print(id(x))

# li = [1, 2, 3, 4]
# a = li
# a.append(6)
# print(li)

# def appen(li):
#     li.append("x")
# li = [1, 2, 3, 4]
# appen(li)
# print(li)

# def toggle(dict):
#     if(dict[1]):
#         dict[1] = False
#     else:
#         dict[1] = True
# dict = {1:True}
# toggle(dict)
# toggle(dict)
# toggle(dict)
# print(dict)

# def toggle(dict):
#     dict.append("a")
# li = []
# toggle(li)
# print(li)

"""
I want you to make a function, that takes 3 arguments/parameters k, x, y
The function should add x, and y, in base-k (let's limit k to max 10)
and the user is not evil (doesn't use digits same or higher than the base)

(base-2) 1 + 1 = 10
0, 1, 10, 11, 100, 101, 110, 111 (base2)
0, 1,  2, 10,  11,  12,  20,  21 (base3)
0, 1,  2,  3,   4,   5,   6,   7 (base10)
(base-4) 321 + 223 = 1210

in base 10, we have 10 digits. 0-9
in base 16, we have 16 digits. 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f.
in base 8, it's 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21
in base 5, it's 0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 20, 21, 22, ..., 44, 100, 101
"""
###
"""
convert from base 10 to base-k (k is always lower than 10, but higher than 1)
input = convert(5, 20)
output = 40

input = convert(2, 255)
output = 11111111

input = convert(5, 200)
output = 1300

input = convert(7, 7)
output = 10

base-k is just -> we have k fingers
since we have (value of 10) fingers, we're used to base-(value of 10)
let's say we have 8 fingers, after 7, it would be 10, then 11, until 17 and then 20

500
HEX base16  1F4
DEC base10  500
OCT base8   764
BIN base2   0001 1111 0100
"""
def convert(k, x):
    #convert x from base 10 to base-k, by brute forcing every number
    y = 0
    while x > 0:
        y += 1
        y = str(y)
        y = list(y)
        y.reverse()
        for i in range(len(y)):
            if int(y[i]) == k:
                y[i] = 0
                if(len(y) - 1 == i):
                    y.append(1)
                else:
                    y[i + 1] = str(int(y[i + 1]) + 1)
        y.reverse()
        y = "".join(y)
        y = int(y)
        x -= 1

print(convert(5, 200))