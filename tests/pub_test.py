import unittest

from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub('The Prancing Pony', 100.00)
        self.drink = Drinks('Wine', 6.50, 4)
        self.customer = Customer('Colin', 8.50, 27)
        self.food = Food('Kebab', 6.00, 4)

    def test_pub_has_name(self):
        self.assertEqual('The Prancing Pony', self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_till_increase_drink(self):
        self.pub.increase_till_cash(self.drink.price)
        self.assertEqual(106.50, self.pub.till)

    def test_pub_till_increase_food(self):
        self.pub.increase_till_cash(self.food.price)
        self.assertEqual(106.00, self.pub.till)

    def test_age_check(self):
        check = self.pub.check_age(self.customer.age)
        self.assertEqual(True, check)
        # solution is far more in depth

    def test_sober(self):
        check = self.pub.check_drunkenness(self.customer.drunkenness)
        self.assertEqual(True, check)
        # This currently takes the customer drunkess value as 0, as from customer.py __init__

    def test_add_stock(self):
        self.pub.add_to_stock('Wine', 6.50, 4)  
        self.pub.add_to_stock('beer', 5.00, 2.8)
            # This works
        # self.pub.add_to_stock(self.drink)
            # This doesn't work, too few arguments
        self.assertEqual(2, len(self.pub.stock))