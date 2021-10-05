#%%
'''
write a program that reads the three edges of a triangle and computes the perimeter if the input is valid.
the input is valid if the sum of every pair of two edges is greater than the remaining edge.
other wise(i.e. else) print a message stating that the input is invalid and the perimeter cannot be calculated.
(note: this question does not require further input validation)

sample output valid case
enter length of edge1: 6.7
enter length of edge2: 9.2
enter length of edge3: 11.6
the perimeter is 27.5

sample output invalid case
enter length of edge1: 16
enter length of edge2: 4.5
enter length of edge3: 23.5
perimeter cannot be calculated: the input is invalid
'''
#%%
edge1 = eval(input("Edge1: "))
edge2 = eval(input("Edge2: "))
edge3 = eval(input("Edge3: "))

if edge1 + edge2 > edge3 and edge1 + edge3 > edge2 and edge2 + edge3 > edge1:
    print(edge1 + edge2 + edge3, "valid")
else:
    print("invalid")
#%%
edge1 = float(input("Enter length of edge 1: "))
edge2 = float(input("Enter length of edge 2: "))
edge3 = float(input("Enter length of edge 3: "))

if edge1 + edge2 > edge3:
    if edge1 + edge3 > edge2:
        if edge2 + edge3 > edge1:
            perimeter = edge1 + edge2 + edge3
            print("The perimeter is", perimeter)
else:
    print("Perimeter cannot be calculated, Invalid input")
#%%
edge1 = float(input("Enter length of edge 1: "))
edge2 = float(input("Enter length of edge 2: "))
edge3 = float(input("Enter length of edge 3: "))

pair1 = edge1 + edge2 > edge3
pair2 = edge1 + edge3 > edge2
pair3 = edge2 + edge3 > edge1

if pair1 and pair2 and pair3:
    perimeter = edge1 + edge2 + edge3
    print("The perimeter is", perimeter)
else:
    print("Perimeter cannot be calculated, Invalid input")