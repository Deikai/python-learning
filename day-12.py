age = 20

print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)
print(age == 20)
print(age != 20)

age = 20
if age >= 18:
    print("You are an adult.")

age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")



age = int(input("How old are you? "))
if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else: 
    print("You are a child.")



age = 16
if age >= 13 and age <= 18:
    print("You are a teenager.")
# This will print if the age is between 13 and 18 (inclusive)

age = 20

if age < 13 or age >= 18:
    print("You are not a teenager.")
# This will print if the age is less than 13 or greater than or equal to 18


# and → todas las condiciones deben ser True
# or  → basta con una condición True
# not → invierte True/False


age = int(input("How old are you? "))
if age < 13:
    print("You are a child.")
elif age >= 13 and age < 18:
    print("You are a teenager.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

