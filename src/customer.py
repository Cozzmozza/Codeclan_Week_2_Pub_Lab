class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0
        # This is our assumption
        # We could add this as an argument if we wanted initial drunkness as they enter the pub

    def reduce_wallet(self, amount):
        self.wallet -= amount
        # Solution: 
        # def reduce_wallet(self, price)
            # self.wallet -= drink.price

    def increase_drunkenness(self, units):
        self.drunkenness += units
        # Solution:
        # def increase_drunkenness(self, drink)
            # self.drunkenness += drink.units

    def decrease_drunkenness(self, units):
        self.drunkenness -= units