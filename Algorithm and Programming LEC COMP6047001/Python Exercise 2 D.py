"""
Software Sales (15 points)

A software company sells a package that retails for $99. Discounts for quantities are given
according to the following table:

Quantity            Discount
10 - 19               10%
20 - 49               20%
50 - 99               30%
100 or more           40%

Write a program that asks the user to enter the number of packages purchased. The program
should then display the amount of the discount (if any) and the total of the purchase after the
discount. (Use appropriate formatting to display currency and percentages in your output.)

Sample output (no discount):
Enter the number of packages purchased  : 5
Discount Amount @ 0%                    : $ 0.00
Total Amount                            : $ 495.00

Sample output (with a discount):
Enter the number of packages purchased  : 45
Discount Amount @ 20%                   : $ 891.00
Total Amount                            : $ 3564.00
"""
qty = int(input("Enter the number of packages purchased: "))
price = 99

if(qty<10):
    disc = 0
elif(qty<20):
    disc = 10
elif(qty<50):
    disc = 20
elif(qty<100):
    disc = 30
else:
    disc = 40

d = price*qty*disc/100
discount = "$ {:,.2f}".format(d)
print(f"Discount Amount @ {disc}%: {discount}")

tot = price*qty*(100-disc)/100
total = "$ {:,.2f}".format(tot)
print(f"Total Amount: {total}")