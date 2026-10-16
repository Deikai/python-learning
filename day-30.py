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
    def show_brand(self):
        print (self.brand) 

    def start(self):
        print("Starting car")

car1 = Car("Toyota")
car1.show_brand()
car1.start()
