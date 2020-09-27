import datetime

class Bakery:

    def __init__(self,stock=0,bill=0):
        """
        Our constructor class.
        """
        self.stock = stock
        self.bill = bill



    def displaystock(self):
        """
        Displays the cakes currently available.
        """
        print("We currently have {} cakes available for delivery.".format(self.stock))
        return self.stock



    def vanilla(self, n):
        """
        Delivers vanilla cake to a customer.
        """
        if n <= 0:
            print("Number of cakes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cakes available for delivery.".format(self.stock))
            return None

        else:
            print("You have selected a {} cake(s) today.".format(n))
            print("You will be charged $5 for each vanilla cake.")

            self.stock -= n




    def chocolate(self, n):
        """
        Delivers chocolate cake to a customer.
        """
        if n <= 0:
            print("Number of cakes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cakes available for delivery.".format(self.stock))
            return None

        else:
            print("You have selected a {} cake(s) today.".format(n))
            print("You will be charged $10 for each chocolate cake.")

            self.stock -= n




    def strawberry(self, n):
        """
        Delivers strawberry cake to a customer.
        """
        if n <= 0:
            print("Number of cakes should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cakes available for delivery.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have selected a {} cake(s) today.".format(n))
            print("You will be charged $12 for each strawberry cake.")

            self.stock -= n





    def totalBill(self, request):
        """
        1. Return a bill
        """
        rentalBasis, numOfCakes = request
        bill = 0

        if rentalBasis and numOfCakes:

            # vanilla
            if rentalBasis == 1:
                bill = bill + (5 * numOfCakes)

            # choco
            elif rentalBasis == 2:
                bill = bill + (10 * numOfCakes)

            # strawberry
            elif rentalBasis == 3:
                bill = bill + (12 * numOfCakes)

            self.bill += bill
            print("That would be ${}".format(self.bill))
            return self.bill
        else:
            print("Total bill is $0")
            return None




class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0


    def requestCake(self):
        """
        Takes a request from the customer for the number of bikes.
        """

        bikes = input("How many cakes would you like? ")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of cakes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes


    def totalBill(self):

        if self.rentalBasis and self.bikes:
            return self.rentalBasis, self.bikes
        else:
            return 0,0
