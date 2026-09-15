person = {
    "name": "Sebastian",
    "age": 28,
    "city": "St. Louis",
    "job": "Developer"
}
# ejemplo de uso de get() con un diccionario

person.get("city", "city not found")
#get devuelve el valor asociado a la clave "city", o "city not found" si la clave no existe
#esta es una forma segura de acceder a los valores de un diccionario sin causar un error si la clave no existe

person["city"]
#esta es una forma de acceder a los valores de un diccionario directamente
#pero puede causar un error si la clave no existe

person.get("name", "Name not found")
if "job" in person:
    print(person["job"])
else:
    print("Job not found")

person.get("name")        # obtiene el valor
print(person.get("Email", "Email not found")) # obtiene y lo muestra

students = [
    {"name": "Ana", "age": 22, "score": 85},
    {"name": "Luis", "age": 28, "score": 90},
    {"name": "Maria", "age": 21, "score": 65},
    {"name": "Carlos", "age": 20, "score": 72}
]

for student in students:
    if student["score"] >= 80:
        print(student["name"], "passed with" , student["score"], "points.")
    else:
        print(student["name"], "failed the exam with" , student["score"], "points.")


# Day 15 - Dictionaries

# Basic dictionary
person = {
    "name": "Sebastian",
    "age": 28,
    "city": "Kansas City",
    "job": "Developer"
}

# Access values
print(person["name"])
print(person["age"])

# Change a value
person["age"] = 29

# Add a new key
person["email"] = "sebastian@email.com"

# Remove a key
person.pop("city")

# Dictionary methods
print(person.keys())
print(person.values())
print(person.items())

# Safe access with get()
print(person.get("name", "Name not found"))
print(person.get("city", "City not found"))

# Check if a key exists
if "job" in person:
    print(person["job"])
else:
    print("Job not found")


# Loop through dictionary
for key, value in person.items():
    print(key, value)


# List of dictionaries
users = [
    {"name": "Sebastian", "age": 27},
    {"name": "Genesis", "age": 26},
    {"name": "Carlos", "age": 30},
]

# Add users
users.append({"name": "Maria", "age": 24})
users.append({"name": "Luis", "age": 35})

# Filter users by age
for user in users:
    if user["age"] >= 30:
        print(user["name"], "is", user["age"], "years old.")


# Student exercise
students = [
    {"name": "Ana", "age": 22, "score": 85},
    {"name": "David", "age": 25, "score": 72},
    {"name": "Maria", "age": 21, "score": 91},
    {"name": "Luis", "age": 24, "score": 65}
]

for student in students:
    if student["score"] >= 80:
        print(student["name"], "passed with", student["score"], "points.")
    else:
        print(student["name"], "failed the exam with", student["score"], "points.")
        