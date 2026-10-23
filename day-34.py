class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self): # string
        return self.name + "-" + str(self.price)
    
    def __eq__(self, other): # equal 
        return self.name == other.name and self.price == other.price
    
    def __lt__(self, other): # less than 
        return self.price < other.price
    
    def __add__(self, other):
        return self.price + other.price

product1 = Product("Keyboard", 50)
print(product1)

class ShoppingCart:
    def __init__(self, products):
        self.products = products

    def __len__(self):
        return len(self.products)
    
    def __contains__(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return True

        return False
    
    def __getitem__(self, index):
        return self.products[index]

product1 = Product("Keyboard", 50)
product2 = Product("Monitor", 250)
product3 = Product("Mouse", 25)

products = [product1, product2, product3]
cart1 = ShoppingCart(products)

print(product1 == product2) # equal este da True
print(product1 == product3) # equal este da False
print(product1 < product2) # less than es para ver cual es el menor en este caso en el precio 
print(product1 + product2) # add or plus es para sumar sus precios 

print("Keyboard" in cart1)
print("Phone" in cart1)
print(cart1[0])

print(len(cart1))
print(cart1[0])
print("Monitor" in cart1)
print(product1 < product2)
print(product1 + product3)
