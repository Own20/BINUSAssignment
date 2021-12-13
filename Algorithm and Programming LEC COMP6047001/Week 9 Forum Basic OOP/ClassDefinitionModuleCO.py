"""
Python Programming Exercise (Basic OOP)

Naming Rule: All module, method and function names (except the __init__ , __str__ and main methods) MUST include your initials at the end of the name.

For example:
• If your class module is called ProgramExercise and your name is John Smith, your class file should be called ProgramExerciseJS
o Try not to call your class file ProgramExercise - pick a name that better suits the content of your class module.
• If your driver module is called ExerciseDriver and your name is John Smith, your class file should be called ExerciseDriverJS
o Try not to call your class file ExerciseDriver - pick a name that better suits the content of your class module.
• If a method is to be called setPrice, and your name is John Smith, your method should be called setPriceJS.
• The init and str method in your class module and the main function in your driver should be the only exceptions to this rule.
• Please include #comments and descriptive “””documentation””” in your code.
• Not following the rules can result in deductions.
• Upload the files in your GitHub repository and share the link on or before 12 midnight on Wednesday, December 8 in the forum thread.
 
Fancy Shopping list
 
A client has asked you to make some unique purchases on their behalf. They are interested in purchasing food from a unique grocery. The grocery specializes in rare (and expensive) food and has a very limited inventory (due in part to rarity of items as well as their commitment to ensuring that all items are ethically sourced). You check out the inventory and find the following items in stock.
 
Food Item Price per Pound (U.S.)
Dry Cured Iberian Ham   $177.80
Wagyu Steaks            $450.00
Matsutake Mushrooms     $272.00
Kopi Luwak Coffee       $306.50
Moose Cheese            $487.20
White Truffles          $3600.00
Blue Fin Tuna           $3603.00
Le Bonnotte Potatoes    $270.81
 
You see this as an opportunity to practice your programming so that you can spend the client's money carefully once they decide which items and amount (in pounds) that they want.
You will write two programs for this endeavor. The first will be a class definition module, and the second will be the driver program. (Remember the naming rules for these modules!)

The class module should contain the following:
 
1. An initializer method that accepts two parameters (other than self):
    a. A parameter corresponding to the name of the food
    b. A parameter corresponding to the amount of the food (in pounds) to order However, the initializer method should contain four hidden attributes:
        a. The name of the food - to be updated using the food parameter
        b. The amount in pounds - to be updated using the amount parameter
        c. The standard price of the food item per pound - to be updated using a private method
        d. The calculated price of the ordered item (based on amount ordered) - to be updated using a public method
 
2. A private method that will store the list of items and their price per pound (in other words, the information provided in the table above).
The method accepts no parameters (other than self) and returns no value.
Use an if-elif structure to set the standard prices of the food.
Reference the hidden attributes of food name and standard price to set the prices.
 
Make sure to include a trailing else that sets the price to 0.00 if an item that is not on the table is referenced (or if an item is misspelled)
 
3. A public method to calculate the cost of the ordered food. The cost should be calculated using the formula:
Amount of food (in pounds) x price per pound
The method accepts no parameters (other than self), but returns the calculated cost.
 
4. Accessors as needed (or an __str__ method if you prefer).
 
Sample output (includes input validation)
 
    How many items will you order today? -1 Number of items must be at least 1.
    How many items will you order today? 4 

    Item #1-
    Enter food: Wagyu Steaks
    Enter amount of pounds: 3
 
    Item #2-
    Enter food: Matsutake Mushrooms
    Enter amount of pounds: 0.5
 
    Item #3-
    Enter food: Le Bonnotte Potatoes
    Enter amount of pounds: 4
 
    Item #4-
    Enter food: Moose Cheese
    Enter amount of pounds: 0
    Amount of pounds must be greater than 0.
    Enter amount of pounds: 1.5

Here's a summary of the items purchased:

    Item: Wagyu Steaks
    Amount ordered: 3.0 pounds
    Price per pound: $450.00
    Price of order: $1350.00
 
    Item: Matsutake Mushrooms
    Amount ordered: 0.5 pounds
    Price per pound: $272.00
    Price of order: $136.00
 
    Item: Le Bonnotte Potatoes
    Amount ordered: 4.0 pounds
    Price per pound: $270.81
    Price of order: $1083.24
 
    Item: Moose Cheese
    Amount ordered: 1.5 pounds
    Price per pound: $487.20
    Price of order: $730.80
 
    Total cost: $3300.04
    Sample output (includes item not on list)
 
How many items will you order today? 2 

    Item #1-
    Enter food: Blue Fin Tuna
    Enter amount of pounds: 2.5
 
    Item #2-
    Enter food: Bacon, lots of Bacon
    Enter amount of pounds: 5

Here's a summary of the items purchased:

    Item: Blue Fin Tuna
    Amount ordered: 2.5 pounds
    Price per pound: $3603.00
    Price of order: $9007.50
 
    Item: Bacon, lots of Bacon
    Amount ordered: 5.0 pounds
    Price per pound: $0.00

    Price of order: $0.00
    Total cost: $9007.50
"""
class MenuCO:
    def __init__(self, name="", amount=0.00):
        self.__name = name
        self.__amount = amount
        self.__standardprice = self.__stanpriceCO()
        self.__calculatedprice = self.__calcpriceCO()
    
    def setNameCO(self, name):
        self.__name = name
    def setAmountCO(self, amount):
        self.__amount = amount
    
    def __stanpriceCO(self):
        if self.__name == 'Dry Cured Iberian Ham':
            self.__standardprice = 177.80
        elif self.__name == 'Wagyu Steaks':
            self.__standardprice = 450.00
        elif self.__name == 'Matsutake Mushrooms':
            self.__standardprice = 272.00
        elif self.__name == 'Kopi Luwak Coffee':
            self.__standardprice = 306.50
        elif self.__name == 'Moose Cheese':
            self.__standardprice = 487.20
        elif self.__name == 'White Truffles':
            self.__standardprice = 3600.00
        elif self.__name == 'Blue Fin Tuna':
            self.__standardprice = 3603.00
        elif self.__name == 'Le Bonnotte Potatoes':
            self.__standardprice = 270.81
        else:
            self.__standardprice = 0.00
        return self.__standardprice

    def __calcpriceCO(self):
        self.__calculatedprice = self.__amount * self.__standardprice
        return self.__calculatedprice
    
    def getNameCO(self):
        return self.__name
    def getAmountCO(self):
        return self.__amount
    def getStanPriceCO(self):
        return self.__standardprice
    def getCalcPriceCO(self):
        return self.__calculatedprice
    
    def __str__(self):
        return f"Item: {self.getNameCO()}\n Amount Ordered: {self.getAmountCO()} pounds\n Price per pound: ${self.__getStanPriceCO():.2f}\n Price of Order: ${self.getCalcPriceCO()}"