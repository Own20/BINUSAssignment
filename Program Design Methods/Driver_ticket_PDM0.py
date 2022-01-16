from Class_ticket_PDM0 import Ticket

print("Code \tTrain name \tDestination \tPrice")
print("--------------------------------------------------")
print("TK001 \tGajayana \tCirebon \tRp.50,000")
print("TK002 \tBima \t\tYogyakarta \tRp.100,000")
print("TK003 \tArgo Bromo \tSurabaya \tRp.200,000")

def buyTicket():
    summary = []

    destination = input("Hello, please enter destination: ")
    if destination == "Cirebon" or "Yogyakarta" or "Surabaya":
        numTicket = int(input("Enter number of ticket: "))
        if numTicket < 1:
            numTicket = int(input("Re-enter valid number of ticket: "))
    else:
        destination = input("Re-enter valid destination: ")

    print()
    summary.append(Ticket(destination, numTicket))

    return summary

def sumTicket(sumTic):
    print("Here's a summary of ticket purchased:")
    print("-------------------------------------")

    for Ticket in sumTic:
        print(f"Train name      : {Ticket.nameTrain()}")
        print(f"Destination     : {Ticket.getDestination()}")
        print(f"Amount tickets  : {Ticket.getNumTicket()}")
        print(f"Total Cost      : Rp.{Ticket.getTotalCost()}")
        print(f"Tickets Left    : {Ticket.processTicket()}")

def main():
    buyTic = buyTicket()
    sumTicket(buyTic)

main()