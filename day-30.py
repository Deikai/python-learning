class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(self.name, "is eating")

class Dog(Animal):
    pass

dog1 = Dog("Max")
dog1.eat()

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Starting vehicle")
    
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_brand(self):
        print (self.brand) 

    def start(self):
        print("Starting car")

car1 = Car("Toyota")
car1.show_brand()
car1.start()

class Truck(Vehicle):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

truck1 = Truck("Ford", 5000)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print("Working")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def work(self):
        print("Writing code.")

class Designer(Employee):
    def work(self):
        print("Designing interface")
    
class Manager(Employee):
    def work(self):
        print("Managing team")  

designer1 = Designer("Maria", 65000)
designer1.work()
developer1 = Developer("Ana", 70000, "Python")
manager1 = Manager("Luis", 80000)

employees = [developer1, designer1, manager1]

for employee in employees:
    employee.work()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade 
    

student1 = Student("Carlos", 20, 85)

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def show_balance(self):
        print(self.balance)

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        self.balance = (self.balance * self.interest_rate) + self.balance

account1 = SavingsAccount("Ana", 1000, 0.05)
account1.add_interest()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print("Woof")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def speak(self):
        print("Meow")

dog1 = Dog("Max")
cat1 = Cat("Luna")

animals = [dog1, cat1]

for animal in animals:
    animal.speak()