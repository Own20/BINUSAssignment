class Ticket:
    def __init__(self, destination="", numTicket=0000):
        self.destination = destination
        self.numTicket = numTicket
        self.fare = self.fromPricelist()
        self.stock = self.checkTicketStock()
        self.name = self.nameTrain()

    def setDestination(self, destination):
        self.destination = destination
    def setNumTicket(self, numTicket):
        self.numTicket = numTicket
    
    def fromPricelist(self):
        if self.destination == "Cirebon":
            self.fare = 50000
        elif self.destination == "Yogyakarta":
            self.fare = 100000
        elif self.destination == "Surabaya":
            self.fare = 200000
        else:
            self.fare = 0
        return self.fare

    def checkTicketStock(self):
        if self.destination == "Cirebon":
            self.stock = 20
        elif self.destination == "Yogyakarta":
            self.stock = 25
        elif self.destination == "Surabaya":
            self.stock = 30
        else:
            self.stock = 0
        return self.stock
    
    def nameTrain(self):
        if self.destination == "Cirebon":
            self.name = "Gajayana (TK001)"
        elif self.destination == "Yogyakarta":
            self.name = "Bima (TK002)"
        elif self.destination == "Surabaya":
            self.name = "Argo Bromo (TK003)"
        else:
            self.name = "none"
        return self.name
    
    def processTicket(self):
        if self.numTicket <= self.stock:
            self.stock -= self.numTicket
        elif self.numTicket > self.stock:
            print("Too much ticket.")
        return self.stock
    
    def getTotalCost(self):
        self.totalCost = self.numTicket * self.fare
        return self.totalCost

    def getDestination(self):
        return self.destination
    def getNumTicket(self):
        return self.numTicket

    # def __str__(self):
    #     return f"Your destination is {self.getDestination()}. \nYour total price will be {self.getTotalCost()}"

    # destination = input("Hello, please enter destination: ")
    # if destination == "Cirebon" and "Yogyakarta" and "Surabaya":
    #     numTicket = int(input("Enter number of ticket: "))
    #     if numTicket < 1:
    #         numTicket = int(input("Re-enter valid number of ticket: "))
    # else:
    #     destination = input("Re-enter valid destination: ")