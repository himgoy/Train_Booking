class Train:

    @staticmethod
    def greet():
        print("Hello User")

    def __init__(self, name, fare, seats, source, destination, trainNo):
        self.trainNo = trainNo
        self.seats = [i for i in range(1, seats + 1)]  # import numpy as np  list(np.arange(1, seats + 1))
        self.capacity = seats
        self.name = name
        self.fare = fare
        self.source = source
        self.destination = destination

    def getTrainInfo(self):
        print(f"Train {self.name}, will start its journey from {self.source} and will end its "
              f"journey at {self.destination}.\nIt will have a fare of Rs.{self.fare} Rupees "
              f"and there will be {len(self.seats)} number of seats present")

    def getStatus(self):
        print(f"**********\n"
              f" The train is {self.trainNo} {self.name}."
              f"There are {len(self.seats)} seats remaining "
              f"\n**********")

    def getFareInfo(self):
        print(f"Cost of fare of {self.name} is Rs.{self.fare}")

    def changeFare(self, newFare):
        self.fare = newFare

    def bookTicket(self):
        if len(self.seats) > 0:
            a = self.seats.pop()
            print(f"Your seat have been booked and your seat number is {a}")
        else:
            print("Sorry, no seats available. Kindly try for another date.")

    def cancelTicket(self, ticketNo):
        if ticketNo <= self.capacity:
            self.seats.append(ticketNo)
            return print(f"Your Ticket No. {ticketNo} has been CANCELLED successfully!!!")
        else:
            return print(f"INVALID ticket No.")


if __name__ == '__main__':
    ashram = Train("Subhash Express", 385, 1000, "Delhi", "Kolkata", 19807)
    ashram.greet()
    ashram.getTrainInfo()
    ashram.changeFare(500)
    ashram.getFareInfo()
    ashram.bookTicket()
    ashram.bookTicket()
    ashram.bookTicket()
    ashram.bookTicket()
    ashram.bookTicket()
    ashram.cancelTicket(1001)
    ashram.cancelTicket(999)
    ashram.bookTicket()
    ashram.bookTicket()
    ashram.getStatus()
