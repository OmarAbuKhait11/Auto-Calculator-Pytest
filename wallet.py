class Wallet(object):
    def __inti__(self, initial_ammount= 0):
        self.balance= initial_ammount

    def withdraw(self, amount):
        self.balance -= amount

    def desposit(self, amount):
        self.balance += amount