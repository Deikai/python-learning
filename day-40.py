import csv

with open("students.csv", "r") as file:
    students = csv.reader(file)
    for student in students:
        print(student)

with open("students.csv", "r") as file:
    students = csv.DictReader(file)
    for student in students:
        print(student["name"])

with open("languages.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["language", "level"])
    writer.writerow(["Python", "Intermdiate"])
    writer.writerow(["JavaScript", "Basic"])
    writer.writerow(["HTML", "Intermediate"])

employees = [
    ["Ana", 45000],
    ["Luis", 60000],
    ["Marta", 52000]
]

with open("employees.csv", "w", newline="") as file:
    writer_employees = csv.writer(file)
    writer_employees.writerow(["name", "salary"])
    writer_employees.writerows(employees)

products = [
    {"name": "Mouse", "price": 25},
    {"name": "Keyboard", "price": 70},
    {"name": "Monitor", "price": 180}
]

with open("products.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price"])
    writer.writeheader()
    writer.writerows(products)

with open("products.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Webcam", 45])

with open("employees.csv", "r") as file:
    employees = csv.DictReader(file)
    for employee in employees:
        salary = int(employee["salary"])
        if salary > 50000:
            print(employee["name"])

with open("products.csv", "r") as file:
    products = csv.DictReader(file)
    expensive_products = []
    for product in products:
        price = int(product["price"])
        if price >= 50:
            expensive_products.append(product)

with open("expensive_products.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "price"])
    writer.writeheader()
    writer.writerows(expensive_products)

games = [
    ["Minecraft", 30],
    ["Hogwarts Legacy", 60],
    ["Days Gone", 40]
]
with open("games.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow("name", "price")
    writer.writerows(games)