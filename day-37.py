double = lambda number: number * 2
is_adult = lambda age: age >= 18
is_more_expensive = lambda price1, price2: price1 > price2

def apply_operation(operation, value):
    return operation(value)

operation = lambda number: number * number

apply_operation(lambda number: number * number, 6)

prices = [10, 20, 30, 40]
new_prices = map(lambda price: price + 5, prices)
print(list(new_prices))

names = ["Sebastian", "Genesis", "Carlos"]
name_upper = map(lambda name: name.upper(), names)
print(list(name_upper))

ages = [14, 22, 17, 30, 18, 15]
is_adult = filter(lambda age: age >= 18, ages)
print(list(is_adult))

prices = [15, 60, 25, 100, 40, 80]
filtered = filter(lambda price: price >= 50, prices)
new = map(lambda number: number - 10, filtered)

products = [
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 180},
    {"name": "Keyboard", "price": 70},
    {"name": "Webcam", "price": 45},
    {"name": "Laptop", "price": 900}
]

filtered2 = filter(lambda product: product["price"] > 50, products)
result = map(lambda product: product["name"], filtered2)
print(list(result))

ordered_products = sorted(products, key = lambda product: product["price"])
reverse_ordered_products = sorted(products, key = lambda product: product["price"], reverse=True)

students = [
    {"name": "Ana", "grade": 85},
    {"name": "Luis", "grade": 58},
    {"name": "Marta", "grade": 92},
    {"name": "Carlos", "grade": 70},
    {"name": "Sofia", "grade": 61}
]

filter_students = filter(lambda student: student["grade"] >= 60, students)
ordered_students = sorted( filter_students, key = lambda student: student["grade"], reverse=True)
name_students = map(lambda student: student["name"], ordered_students)
print(list(name_students))

products = [
    {"name": "Mouse", "price": 25, "stock": 10},
    {"name": "Monitor", "price": 180, "stock": 0},
    {"name": "Keyboard", "price": 70, "stock": 5},
    {"name": "Webcam", "price": 45, "stock": 8},
    {"name": "Laptop", "price": 900, "stock": 2},
]

filter_products = filter(lambda product: product["stock"] > 0 and product["price"] >= 50, products)
ordered_product = sorted(filter_products, key=lambda product: product["price"], reverse=True)
name_product = map(lambda product: product["name"], ordered_product)
print(list(name_product))
