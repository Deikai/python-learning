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
        self.__money = money

    def add_money(self, amount):
        if amount > 0:
            self.__money = self.__money + amount

    def get_money(self):
        return self.__money

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__money:
            self.__money = self.__money - amount
    
    @property
    def money(self):
        return self.__money
    
    @money.setter
    def money(self, value):
        if value >= 0:
            self.__money = value
        else:
            print("Invalid amount")

wallet1 = Wallet("Sebastian", 100)
wallet1.add_money(50)
wallet1.withdraw(40)
print(wallet1.get_money()) 
print(wallet1.money)
wallet1.money = 200
print(wallet1.money)


class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock
    
    @property
    def stock(self):
        return self.__stock

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 0:
            self.__price = value
        else:
            print("Invalid price")
            self.__price = 0

    def restock(self, amount):
        if amount > 0:
            self.__stock = self.__stock + amount

    def sell(self, amount):
        if amount > 0 and amount <= self.__stock:
            self.__stock = self.__stock - amount
    
    @property
    def inventory_value(self):
        return self.__stock * self.__price
    
    @property
    def is_available(self):
        if self.__stock > 0:
            return True
        else:
            return False



product1 = Product("Keyboard", 50, 10)
product1.restock(5)
product1.sell(3)
print(product1.inventory_value)
product1.is_available

class BankAccount:
    def __init__(self, owner, balance, pin):
        self.owner = owner
        self.__balance = balance
        self.__pin = pin
    
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Incorrect PIN")
        if amount > self.__balance:
            print("Insufficient balance")
        if amount > 0:
            self.__balance = self.__balance - amount

        print(self.__balance)

account1 = BankAccount("Sebastian", 1000, 1234)
account1.deposit(500)
account1.withdraw(200, 1234)
account1.balance