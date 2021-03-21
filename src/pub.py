class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.stock = {}

    def increase_till_cash(self, amount):
        self.till += amount

    def check_age(self, customer_age):
        return customer_age >= 18

    # Solution to check age - 
    # def serve(self, customer, drink):
    #     if self.drinks.count(drink) != 0:
    #       self.drinks.remove(drink)
    #       customer.buy_drink(drink)
    #       self.till += drink.price

    def check_drunkenness(self, customer_drunkenness):
        return customer_drunkenness < 40
        # # Checks how drunk the customer is
        # if customer_drunkenness < 40:
        #     return True
        # return False

    def add_to_stock(self, name, price, alcohol_level):
        self.stock['name'] = {'price' : price, 'alcohol_level' : alcohol_level}
        # THis works for adding 1 entry, but fails for 2
        # self.stock['name'] = {'price' : price, 'alcohol_level' : alcohol_level}
        
        # # data.update({})
        # self.stock.update(name)
        # self.stock.name.update({'price' : price, 'alcohol_level' : alcohol_level})