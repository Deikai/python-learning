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

developer1 = Developer("Ana", 70000, "Python")

class Designer(Employee):
    def work(self):
        print("Disigning interface")

designer1 = Designer("Maria", 65000)
designer1.work()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade 

student1 = Student("Carlos", 20, 85)

