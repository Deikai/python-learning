import json

student = {
    "name": "Sebastian",
    "age": 27,
    "learning": "Python"
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    student = json.load(file)
    print(student["learning"])

users = [
    {"name": "Ana", "age": 25},
    {"name": "Luis", "age": 31},
    {"name": "Marta", "age": 22}
] 

with open("users.json", "w") as file:
    json.dump(users, file)

with open("users.json", "r") as file:
    users = json.load(file)
    for user in users:
        print(user["name"])

car = {
    "brand": "Toyota",
    "year": 2024
}

json_text = json.dumps(car)
print(json_text)

user_text = '{"name": "Carlos", "age": 30}'
user = json.loads(user_text)
print(user["name"])

with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

with open("users.json", "r") as file:
    users = json.load(file)
    for user in users:
        if user["name"] == "Ana":
            user["age"] = 26

with open("users.json", "w")as file:
    json.dump(users, file, indent=4)

profile = {
    "username": "Sebastian",
    "email": "sebastian@example.com",
    "age": 27
}
with open("profile.json", "w") as file:
    json.dump(profile, file, indent=4, sort_keys=True)

store = {
    "name": "Tech Store",
    "location": {
        "city": "Kansas City",
        "country": "USA"
    },
    "Products": [
        {"name": "Mouse", "price": 25},
        {"name": "Keyboard", "price": 70}
    ]
}

with open("store.json", "w") as file:
    json.dump(store, file, indent=4)

with open("store.json", "r") as file:
    store = json.load(file)
    for item in store["Products"]:
        if item["name"] == "Keyboard":
            print(item["price"])
