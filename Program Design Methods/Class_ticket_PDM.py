class Ticket:
    def __init__(self, destination, numTicket):
        self.destination = destination
        self.checkTicketStock(numTicket)
        self.fare = self.fromPricelist()
        self.stock = self.checkTicketStock()
    
    def fromPricelist(self):
        if self.destination == "Cirebon":
            self.fare = 50000
        elif self.destination == "Yogyakarta":
            self.fare = 100000
        elif self.destination == "Surabaya":
            self.fare = 200000
        return self.fare

    def checkTicketStock(self, numTicket):
        if self.destination == "Cirebon":
            self.stock = 20
            if numTicket <= self.stock:
                self.numTicket = numTicket
                self.stock -= numTicket
        elif self.destination == "Yogyakarta":
            self.stock = 25
            if numTicket <= self.stock:
                self.numTicket = numTicket
                self.stock -= numTicket
        elif self.destination == "Surabaya":
            self.stock = 30
            if numTicket <= self.stock:
                self.numTicket = numTicket
                self.stock -= numTicket
        else:
            print("Not enough ticket.")
    
    def setDestination(self, destination):
        self.destination = destination
    
    # def getTotalCost(self):
    #     return self.numTicket * self.fare

    def getDestination(self):
        return self.destination

    # def __str__(self):
    #     return f"Your destination is {self.getDestination()}. \nYour total price will be {self.getTotalCost()}"