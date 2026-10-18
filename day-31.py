class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

engine1 = Engine()
car1 = Car("Toyota", engine1)
car1.engine
car1.engine.start()

class Battery:
    def __init__(self, level):
        self.level = level

    def show_level(self):
        print("Battery level: ", self.level)
    
    def use(self, amount):
        if self.level == 0 or amount == 0:
            return None
        if amount <= self.level:
            self.level = self.level - amount
            print(self.level)

class Phone:
    def __init__(self, brand, battery, camera):
        self.brand = brand
        self.battery = battery
        self.camera = camera

    def check_battery(self):
        self.battery.show_level()
    
    def use_battery(self, amount):
        self.battery.use(amount)

    def take_picture(self):
        self.camera.take_photo()
        self.battery.use(5)

class Camera:
    def take_photo(self):
        print("Taking photo")
        

battery1 = Battery(75)
camera1 = Camera()
phone1 = Phone("Samsung", battery1, camera1)
phone1.battery.show_level()
phone1.check_battery()
phone1.use_battery(20)
phone1.take_picture()

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def total(self):
        total = 0
        for product in self.products:
            total = total + product.price 

        return total
    
    def add_product(self, product):
        self.products.append(product)
    
    def show_products(self):
        for product in self.products:
            print(product.name)

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

product1 = Product("Keyboard", 50)
product2 = Product("Mouse", 25)
product3 = Product("Monitor", 200)
product4 = Product("Headphones", 100)
products = [product1, product2, product3]
cart1 = ShoppingCart(products)
cart1.total()
cart1.add_product(product4)
cart1.show_products()

found = cart1.find_product("Monitor")

if found != None:
    print(found.price)
else:
    print("Product not found")
