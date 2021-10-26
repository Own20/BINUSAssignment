"""
1. Write a function called convert to days() that takes no parameters. Have your function prompt the user to input numbers of hours, minutes, and seconds. Write a helper function called get days() that uses these values and converts them to days in float form (fractions of a day are allowed). get days() should return the number of days. Use this helper function within the convert to days() function to display the numbers of days to the user. The built-in function round() takes two arguments: a number and an integer indicating the desired precision (i.e., the desired number of digits beyond the decimal point). Use this function to round the number of days four digits after the decimal point.

The following demonstrates the proper behavior of convert to days():
convert_to_days()
Enter number of hours   : 97
Enter number of minutes : 54
Enter number of seconds : 45
The number of days is   : 4.0797
"""
def convert_to_days():
    hour   = int(input("Enter number of hours: "))
    minute = int(input("Enter number of minutes: "))
    second = int(input("Enter number of seconds: "))
    return hour, minute, second

h, m, s = convert_to_days()

min = s / 60                #converting seconds to minutes
minutes = m + min           #total minutes
hr = minutes / 60           #converting minutes to hours
hours = h + hr              #total hours
days = hours / 24           #converting hours to days
res = round(days, 4)        #rounding the number of days to four decimal places

print(f"The number of days is: {res}")

#below is to test the numbers after math process
# print(h)
# print(m)
# print(s)
# print(min)
# print(minutes)
# print(hr)
# print(hours)
# print(days)
# print(res)