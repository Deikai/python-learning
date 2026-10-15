numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]


numbers = [3, 7 ,10, 15, 20, 25]
greater_than_10 = [number for number in numbers if number > 10]

scores = [55, 80, 45, 90, 70]
results = ["Pass" if score >= 70 else "Fail" for score in scores]

words = ["Python", "Git", "HTML", "JavaScript", "CSS"]
short_words = [word for word in words if len(word) < 4]

numbers = [1, 2, 3, 4, 5, 6]
even_squares = [number * number for number in numbers if number % 2 == 0]

numbers = [2, 5, 8, 11, 14, 17]
doubled_even = [number * 2 for number in numbers if number % 2 == 0]

students = [
    {"name": "Ana", "grade": 85},
    {"name": "Luis", "grade": 60},
    {"name": "Maia", "grade": 92}
]

passed_students = [student["name"] for student in students if student["grade"] >= 70]

products = [
    {"name": "Keyboard", "price": 50, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Monitor", "price": 200, "stock": 2},
    {"name": "Cable", "price": 10, "stock": 6}
]

available_cheap = [product["name"] for product in products if product["price"] <= 50 and product["stock"] > 0]

def add_tax(price):
    return price * 1.10

prices = [10, 20, 50]

prices_with_tax = [add_tax(price) for price in prices]

numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]

flat_numbers = [number for group in numbers for number in group ]

groups = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8]
]

even_numbers = [ number for group in groups for number in group if number % 2 == 0]

products = [
    {"name": "Keyboard", "price": 50, "stock": 4},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Monitor", "price": 200, "stock": 2},
    {"name": "Cable", "price": 10, "stock": 0}
]

def available_products(products):
    return [product["name"] for product in products if product["stock"] > 0]

products = [
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200}
]

product_tuples = [(product["name"], product["price"]) for product in products]

products = [
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25},
    {"name": "Monitor", "price": 200},
    {"name": "Cable", "price": 10}
]
def affordable_products(products, max_price):
    return [(product["name"], product["price"]) for product in products if product["price"] <= max_price]

students = [
    {"name": "Ana", "grade": 85},
    {"name": "Luis", "grade": 60},
    {"name": "Maria", "grade": 92},
    {"name": "Carlos", "grade": 70},
    {"name": "Sofia", "grade": 55}
]

def passed_student_names(students):
    return [student["name"] for student in students if student["grade"] >= 70]

