# from Week8ExerciseJustForFun import Pet

# p1 = Pet()

# print("A pet object has been created. Here is the initial information about the pet:")
# print(p1.__str__())

# print("Let's update the information for a pet!")
# name = input("Enter the pet's name: ")
# type = input("Enter the type of animal: ")
# age = input("Enter the pet's age: ")

# p2 = Pet(name, type, age)

# print("")
# print("Here is the updated information about the pet:")
# print(p2.__str__())

from Week8ExerciseJustForFun import Retail_item

summary = Retail_item()

name1 = input("Name of item 1: ")
amount1 = float(input("Amount of item 1: "))
price1 = float(input("Price of item 1: "))

nameitem1 = summary.setName(name1)
amountitem1 = summary.setAmount(amount1)
priceitem1 = summary.setPrice(price1)

detailsitem1 = summary.__str__

print("")
name2 = input("Name of item 2: ")
amount2 = float(input("Amount of item 2: "))
price2 = float(input("Price of item 2: "))

nameitem2 = summary.setName(name2)
amountitem2 = summary.setAmount(amount2)
priceitem2 = summary.setPrice(price2)

detailsitem2 = summary.__str__

print("")
print("Here is a summary of the items you added:")
print("Item \t Amount \t Price")
print("-------------------------------")
print(detailsitem1)
print(detailsitem2)