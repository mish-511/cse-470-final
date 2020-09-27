from model import Bakery, Customer
from view import Choose

class Home():

    def home():
        shop = Bakery(100)
        customer = Customer()

        while True:
            print(Choose.choices())

            choice = input("Enter choice: ")

            try:
                choice = int(choice)
            except ValueError:
                print("That's not an integer!")
                continue

            if choice == 1:
                shop.displaystock()

            elif choice == 2:
                customer.rentalTime = shop.vanilla(customer.requestCake())
                customer.rentalBasis = 1

            elif choice == 3:
                customer.rentalTime = shop.chocolate(customer.requestCake())
                customer.rentalBasis = 2

            elif choice == 4:
                customer.rentalTime = shop.strawberry(customer.requestCake())
                customer.rentalBasis = 3

            elif choice == 5:
                customer.bill = shop.totalBill(customer.totalBill())
                customer.rentalBasis, customer.bikes = 0,0

            elif choice == 6:
                break

            else:
                print("Invalid input. Please enter number between 1-6 ")
        print("Thank you for using our bakery.")


    home()
