class Retail_Item:

    # Instantiation
    def __init__(self, type="Not Specified", amount=0, price=0.00):
        self.__type = str(type)
        self.__amount = int(amount)
        self.__price = float(price)

    # Mutator methods
    def setType(self, type):
        self.__type = type
    def setAmount(self, amount):
        self.__amount = amount
    def setPrice(self, price):
        self.__price = price

    # Accessor methods
    def getType(self):
        return self.__type
    def getAmount(self):
        return self.__amount
    def getPrice(self):
        return self.__price

    # Prints formatted string when called
    def __str__(self):
        return f"{self.getType()}\t\t\t{self.getAmount()}\t\t${self.getPrice():.2f}"

# def main():
#     name1 = input("Name of item 1: ")
#     amount1 = int(input("Amount of item 1: "))
#     price1 = float(input("Price of item 1: "))

#     name2 = input("Name of item 2: ")
#     amount2 = int(input("Amount of item 2: "))
#     price2 = float(input("Price of item 2: "))

#     item1 = Retail_Item(name1, amount1, price1)
#     item2 = Retail_Item(name2, amount2, price2)
    
#     print("Item\t\t\tAmount\t\tPrice")
#     print("-----------------------------------------------")
#     print(item1)
#     print(item2)

def mainloop():
    count = int(input("How many items do you want to buy? >> "))
    li = []

    for i in range(count):
        name = input(f"Name of item {i}: ")
        amount = int(input(f"Amount of item {i}: "))
        price = float(input(f"Price of item {i}: "))
        print("")
        
        li.append(Retail_Item(name, amount, price))

    print("Item\t\t\tAmount\t\tPrice")
    print("-----------------------------------------------")
    for i in li:
        print(i)

if __name__ == "__main__":
    # main()
    mainloop()