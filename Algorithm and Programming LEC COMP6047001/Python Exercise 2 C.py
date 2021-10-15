"""
Wind-Chill Temperature (15 points)

In 2001, the National Weather Service implemented a new wind-chill temperature formula to
measure the coldness using temperature and wind speed. The formula is:

twc = 35.74 + 0.6215ta - 35.75v0.16 + 0.4275tav0.16

where:
twc is the wind chill temperature
ta is the outside temperature
v is the wind speed

The formula can only be used for temperatures between -58 degrees Fahrenheit and 41
degrees Fahrenheit, as well as wind speeds greater than or equal to 2mph.

Write a program that:
• asks the user to enter a temperature between -58 degrees Fahrenheit and 41 degrees
Fahrenheit.
o Input validation: If the user enters a temperature not in range, use an if
statement or while loop to ask them to re-enter the value.
• asks the user to enter a windchill greater than 2mph.
o Input validation: If the user enters a wind speed not in range, use an if statement
or while loop to ask them to re-enter the value.

The program then calculates the wind-chill temperature using the formula above. Format the
output to 3 decimal places.

Sample output (including input validation):
Enter the temperature in Fahrenheit             : -60
Temperature must be between                     : -58F and 41F
Please re-enter the temperature in Fahrenheit   : 50
Temperature must be between                     : -58F and 41F
Please re-enter the temperature in Fahrenheit   : 35
Enter the wind speed miles per hour             : -1
Speed must be greater than or equal to          : 2
Please re-enter the wind speed miles per hour   : 5
The wind chill index is                         : 30.600
"""
fahr = True

while(fahr):
    temp = int(input("Enter the temperature in Fahrenheit: "))
    if(-58<temp<41):
        fahr = False
    else:
        print("Please re-enter the temperature in Fahrenheit (Temperature must be between -58F and 41F)")

mile = True

while(mile):
    speed = int(input("Enter the wind speed miles per hour: "))
    if(speed>=2):
        mile = False
    else:
        print("Please re-enter the wind speed miles per hour (Speed must be greater than or equal to 2)")

ta = temp
v = speed
twc = 35.74 + 0.6215*ta - 35.75*v**0.16 + 0.4275*ta*v**0.16
twc = "{:.3f}".format(twc)

print(f"The wind chill index is {twc}")