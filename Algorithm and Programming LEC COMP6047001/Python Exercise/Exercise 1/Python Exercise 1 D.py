"""
Area of a Hexagon (15 points)
Write a program that prompts the user to enter the side of a hexagon and displays its area. The
area of a hexagon is 3v3/2*s**2. Assume that the side entered is positive.

Format the result to three decimal places. Use the functions pow and sqrt from the math
module to express the formula accurately. (See section 2.9 in your zyBook to review the math
module.)

Sample output:
Enter the side length of the hexagon: 5.5
The area of a hexagon with side length 5.5 is 78.592
"""
from fractions import Fraction
import math
s = float(input("Enter the side length of the hexagon: "))

form = float(s**2) * (Fraction(3*math.sqrt(3)/2))
formula = "{:.3f}".format(form)

print(f"The area of a hexagon with side length {s} is {formula}")