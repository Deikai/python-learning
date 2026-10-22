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

def most_expensive_product(products):
    highest_price = None
    most_expensive = None
    for name, price, stock in products:
        if highest_price is None or highest_price < price:
            highest_price = price
            most_expensive = name
    return most_expensive

numbers = [1, 2, 3]
numbers_tuple = tuple(numbers) # esto funciona para convertir una lista en una tupla

number = (1, 2, 3)
number_list = list(number) # hace lo mismo pero transforma la tupla en lista

languages = ["Python", "JavaScript", "HTML"]
languages_tuple = tuple(lenguages)

language_tuple = ("Python", "JavaScript", "HTML")
language_list = list(language_tuple)

tools = ("Git", "Docker", "VS Code")
tools_list = list(tools)
tools_list[1] = "GitHub"
tools = tuple(tools_list)