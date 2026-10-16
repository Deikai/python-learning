class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

car1 = Car("Toyota", 2020)
car1.brand # es "Toyota"
car1.year # es 2020

class Dog:
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")
    
    def introduce(self):
        print("My name is", self.name)

    def eat(self, food):
        print(self.name, "is eating", food)

    def play(self, toy):
        print(self.name, "is playing with", toy)

    def birthday(self):
        self.age = self.age + 1

    def get_age(self):
        return self.age

    def get_info(self):
        return (self.name, self.age)

dog1 = Dog("Max", 4)
dog1.bark()
dog1.introduce()
dog1.eat("Chicken")
dog1.play("ball")
dog1.birthday()
age = dog1.get_age()
info = dog1.get_info()


dog2 = Dog("Rocky", 2)
dog2.birthday()
dog2.birthday()

class BankAcount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def transfer(self, other_account, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            other_account.deposit(amount)

account1 = BankAcount("Sebastian", 100)
account1.deposit(50)

account2 = BankAcount("Ana", 50)

account1.transfer(account2, 50)

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, selll):
        if self.stock >= selll:
            self.stock = self.stock - selll
    
    def inventory_value(self):
        return self.stock * self.price
    
    def restock(self, amount):
        self.stock = self.stock + amount
        return self.stock

product1 = Product("Keyboard", 50, 10)
product1.sell(3)
product1.inventory_value()
product1.restock(5)


