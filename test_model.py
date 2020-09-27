import unittest
from unittest.mock import patch
from model import Bakery, Customer

class TestBakery(unittest.TestCase):

    def test_stock(self):
        self.stock=100
        result = Bakery.displaystock(self)
        self.assertIsNotNone(result)


    def test_vanilla_a(self):
        self.stock=100
        result = Bakery.vanilla(self,-1)
        self.assertIsNone(result)

    def test_vanilla_b(self):
        self.stock=100
        result = Bakery.vanilla(self,1000)
        self.assertIsNone(result)

    def test_vanilla_c(self):
        self.stock=100
        result = Bakery.vanilla(self,10)
        self.assertIsNone(result)



    def test_chocolate_a(self):
        self.stock=100
        result = Bakery.chocolate(self,-1)
        self.assertIsNone(result)

    def test_chocolate_b(self):
        self.stock=100
        result = Bakery.chocolate(self,1000)
        self.assertIsNone(result)

    def test_chocolate_c(self):
        self.stock=100
        result = Bakery.chocolate(self,10)
        self.assertIsNone(result)



    def test_strawberry_a(self):
        self.stock=100
        result = Bakery.strawberry(self,-1)
        self.assertIsNone(result)

    def test_strawberry_b(self):
        self.stock=100
        result = Bakery.strawberry(self,1000)
        self.assertIsNone(result)

    def test_strawberry_c(self):
        self.stock=100
        result = Bakery.strawberry(self,10)
        self.assertIsNone(result)




class TestCustomer(unittest.TestCase):

    def test_requestCake(self):
        result = Customer.requestCake(self)
        self.assertIsNotNone(result)




if __name__=='__main__':
    unittest.main()
