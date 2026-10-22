class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return self.name + "-" + str(self.price)

product1 = Product("Keyboard", 50)
print(product1)
