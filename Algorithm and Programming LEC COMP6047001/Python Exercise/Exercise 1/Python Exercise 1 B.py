"""
Runway Length (15 points)
Given an airplane’s acceleration, a, and take-off speed, v, the minimum runway length needed
for the airplane to take off is computed using the formula v^2/2a

Write a program that prompts the user to enter the speed in meters per second (m/s) and the
acceleration in meters per second squared (m/s2). The program should calculate and display the
minimum runway length. Format the result to four decimal places. (For this question, assume
that all values entered are positive.)

Sample output:
Enter the plane's take off speed in m/s: 60
Enter the plane's acceleration in m/s**2: 3.5
The minimum runway length needed for this airplane is 514.2857 meters.
"""
v = float(input("Enter airplane's take-off speed in m/s: "))
a = float(input("Enter airplane's acceleration in m/s**2: "))

formula = (v**2)/(2*a)
runway = "{:.4f} meters".format(formula)

print(f"The minimum runway length needed for this airplane is {runway}")