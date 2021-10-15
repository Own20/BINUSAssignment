"""
Tip Calculator (15 points)
Write a program that reads the subtotal and gratuity rate. The program then calculates and
gratuity as a dollar amount, followed by the total amount, and displays all information in
dollars.

Your code should include currency formatting (i.e., use the $ in your output, include comma
separation and format the result to 2 decimal places.)

Sample output:
Enter the subtotal          : $1250
Enter tip amount (as a %)   : 25
Subtotal                    : $ 1,250.00
Tip                         : $ 312.50
Total                       : $ 1,562.50
"""
s = float(input("Enter the subtotal: "))
t = float(input("Enter tip amount (as a %): "))

ti = t/100*s

sub = "$ {:,.2f}".format(s)
tip = "$ {:,.2f}".format(ti)

print(f"Subtotal: {sub}")
print(f"Tip: {tip}")

tot = s+ti
total = "$ {:,.2f}".format(tot)
print(f"Total: {total}")