"""
Perimeter of a triangle (15 points)

Write a program that reads the three edges of a triangle and computes the perimeter if the input is valid. The input is valid if the sum of every pair of two edges is greater than the remaining edge. Otherwise (i.e. else) print a message stating that the input is invalid and the perimeter cannot be calculated.
(Note: This question does NOT require further input validation.)

Sample output (Valid case):
Enter length of edge1: 6.7
Enter length of edge2: 9.2
Enter length of edge3: 11.6
The perimeter is 27.5

Sample output (Invalid case):
Enter length of edge1: 16
Enter length of edge2: 4.5
Enter length of edge3: 23.5
Perimeter cannot be calculated: the input is invalid.
"""
edge1 = float(input("Enter length of edge1: "))
edge2 = float(input("Enter length of edge2: "))
edge3 = float(input("Enter length of edge3: "))

pair1 = edge1 + edge2 > edge3
pair2 = edge1 + edge3 > edge2
pair3 = edge2 + edge3 > edge1

if pair1 and pair2 and pair3:
    perimeter = edge1 + edge2 + edge3
    print(f"The perimeter is {perimeter}")
else:
    print("Perimeter cannot be calculated: the input is invalid.")