# Instructions:
# Please read carefully. If anything is unclear, do your best to interpret,list any assumptions, discuss it in the thread, and put it as a comment in your scripts.
 
# Fractions and Mixed Numbers
 
# An elementary school teacher has asked for your help in teaching their students about types of fractions, as well as reducing (or simplifying) fractions.
# The teacher shows you the image https://www.cuemath.com/numbers/types-of-fractions/ to illustrate how they taught the class about the types of fractions (and the condition for proper and improper fractions).
# The teacher also reminds you that a fraction cannot be reduced if the greatest common divisor (gcd) is 1; if it is not 1, the gcd can be used to reduce the fraction by dividing both the numerator and the denominator by the gcd. 
# Thanks to this information, you are ready to begin programming!
# Your program should do the following:
 
# 1) Ask the user to enter a numerator and denominator. Use input validation to ensure that both the numerator and denominator are positive. (Note: 0 is not considered positive.)
# 2) Calculate the greatest common divisor (gcd) using the gcd function from the math module. The function can be used as: math.gcd(a,b) where a and b are the numerator and denominator respectively. Don’t forget to include the math module!
 
# For number 3 - 7 (You may or may not follow this, this is just a "guide" to help you solve the problem. Do not restrict yourself to follow this, be creative and solve the problem as you see fit.
 
# 3) Create an (outer) if else statement that determines whether the fraction is proper or improper. If the fraction is proper, display the fraction and state that it is proper; otherwise, it is improper.
# 4) Create a nested if else statement - within the if clause of part 3 - to check if the proper fraction can be reduced. If it can’t, display a message indicating that the proper fraction can’t be reduced; otherwise, reduce the fraction and display the reduced form.
# 5) In the else clause of part 3, create another nested if else statement to check if the improper fraction can be reduced. Once again, if it can’t, display a message indicating that the improper fraction can’t be reduced; otherwise, reduce the fraction and display the reduced form.
# 6) The improper fraction must be converted to a mixed number, regardless of whether the it can be reduced. Use integer division and the modulus to calculate the mixed number. (This calculation is necessary in both the nested if and else clauses in part 5.)
# 7) Finally, if the fractional portion of the mixed number is 0, only display the whole number (i.e. do not display a fraction as 0 / b). Use another nested if else statement to display the mixed number appropriately. (This nested if else statement should also be in both the if and else clauses in part 5, after calculating the mixed number.)
 
# Sample outputs are shown below:
# Sample 1 (input validation and proper fraction check, no reduction):
# Enter a numerator: Value must be greater than 0               : -3
# Please re-enter the numerator. Value must be greater than 0   : 3
# Enter a denominator. Value must be greater than 0             : -7
# Please re-enter the denominator. Value must be greater than 0 : 7
# 3 / 7 is a proper fraction.
# This proper fraction cannot be reduced any further.
 
# Sample 2 (proper fraction, reduced):
# Enter a numerator: Value must be greater than 0               : 10
# Enter a denominator. Value must be greater than 0             : 15
# 10 / 15 is a proper fraction.
# This proper fraction can be reduced to                        : 2 / 3

# Sample 3 (improper fraction, no reduction, mixed number):
# Enter a numerator: Value must be greater than 0               : 78
# Enter a denominator. Value must be greater than 0             : 11
# 78 / 11 is an improper fraction.
# This improper fraction cannot be reduced any further.
# The mixed number is 7 and 1 / 11
 
# Sample 4 (improper fraction, reduction, mixed number)
# Enter a numerator: Value must be greater than 0               : 6
# Enter a denominator. Value must be greater than 0             : 4
# 6 / 4 is an improper fraction.
# This improper fraction can be reduced to: 3 / 2
# The mixed number is 1 and 1 / 2
 
# Sample 5 (improper fraction, reduction, whole number)
# Enter a numerator: Value must be greater than 0               : 8
# Enter a denominator. Value must be greater than 0             : 2
# 8 / 2 is an improper fraction.
# This improper fraction can be reduced to                      : 4 / 1
# The whole number is 4
 
# Sample 6 (improper fraction, no reduction, whole number)
# Enter a numerator: Value must be greater than 0               : 11
# Enter a denominator. Value must be greater than 0             : 1
# 11 / 1 is an improper fraction.
# This improper fraction cannot be reduced any further.
# The whole number is 11
 
# Tip: Check your indentation carefully for this exercise, especially for the improper fractions portion of your code.

import math

n = int(input("Enter a numerator: "))
d = int(input("Enter a denominator: "))

while(n < 1):
    print("Value must be greater than 0")
    n = int(input("Re-enter a numerator : "))
while(d < 1):
    print("Value must be greater than 0")
    d = int(input("Re-enter a denominator : "))

gcd = math.gcd(n, d)

if n < d:
    print(f"{n} / {d} is a proper fraction")
    if gcd == 1:
        print("The proper fraction cannot be reduced")
    elif gcd != 1:
        n //= gcd
        d //= gcd
        print(f"This proper fraction can be reduced to: {n} / {d}")
elif n >= d:
    print(f"{n} / {d} is an improper fraction")
    if gcd == 1:
        print("The improper fraction cannot be reduced")
    elif gcd != 1:
        n //= gcd
        d //= gcd
        print(f"This improper fraction can be reduced to : {n} / {d}")
    frac = n // d
    r = n % d
    if r != 0:
        print(f"The mixed number is {frac} and {r} / {d}")
    elif r == 0:
        print(f"The whole number is {frac}")