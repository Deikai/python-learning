class BankAccount:
    def __init__(self, owner, _balance):
        self.owner = owner
        self._balance = _balance

    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount

account1 = BankAccount("Sebas", 500)
account1.deposit(100)

class Wallet:
    def __init__(self, owner, money):
        self.owner = owner
        self._money = money

    def add_money(self, amount):
        if amount > 0:
            self._money = self._money + amount

    def get_money(self):
        return self._money

    def withdraw(self, amount):
        if amount > 0 and amount <= self._money:
            self._money = self._money - amount

wallet1 = Wallet("Sebastian", 100)
wallet1.add_money(50)
print(wallet1.get_money()) 