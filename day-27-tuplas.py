profile = ("Sebastian", 27, "Python")
name = profile[0]
age = profile[1]
technology = profile[2]

person = ("Ana", 24, "JavaScript")

name2, age2, technology2 = person

skills = ("Python", "Git", "HTML", "Python", "CSS", "Python")

python_count = skills.count("Python")
git_position = skills.index("Git")

lenguage = ("Python",)
number = (27,)

technologies = ("Python", "Git", "HTML", "CSS", "JavaScript")
web = technologies[2:]
last_two = technologies[-2:]

languages = ("Python", "JavaScript")
tools = ("Git", "Docker")
stack = languages + tools

numbers = (1, 2)
repeated = (1, 2) * 3

prices = (15, 20, 35, 10)
for price in prices:
    print(price)

total = 0
for price in prices:
    total = total + price
print (total)

def product_info():
    return "Keyboard", 50
product_name, product_price = product_info()

def coordinates():
    return 39.1, -94.5
latitude, longitude = coordinates()

products = [
    ("Keyboard", 50),
    ("Mouse", 25),
    ("Monitor", 200)
]
for name, price in products:
    print (name)

for name, price in products:
    if price > 30:
        print (name)

products = [
    ("Keyboard", 50, 4),
    ("Mouse", 25, 8),
    ("Monitor", 200, 2)
]

def inventory_value(products):
    total = 0
    for name, price, stock in products:
        total = total + price * stock
    return total