# Day 16 - Functions

# Basic function
def greet():
    print("Hello!")

greet()


# Funcion con un parámetro
def greet_name(name):
    print("Hello", name)

greet_name("Sebastian")
greet_name("Genesis")


# Funcion con dos parámetros
def introduce(name, age):
    print("My name is", name)
    print("I am", age, "years old.")

introduce("Sebastian", 27)


# Funcion con return
def add(a, b):
    return a + b

result = add(5, 3)
print(result)


# Usando el valor return en otra operación
total = add(5, 3) * 2
print(total)


# Function with if / elif / else
def check_age(age):
    if age < 13:
        return "Child"
    elif age >= 18:
        return "Adult"
    else:
        return "Teenager"

print(check_age(10))
print(check_age(15))
print(check_age(20))


# Default parameter
def greet_guest(name="Guest"):
    print("Hello", name)

greet_guest("Carlos")
greet_guest()


# One required parameter and one default parameter
def show_job(name, job="Developer"):
    print(name, "works as a", job)

show_job("Sebastian")
show_job("Carlos", "Designer")


# Two default parameters
def show_profile(name="Guest", job="Developer"):
    print(name, "works as a", job)

show_profile()
show_profile("Sebastian")
show_profile("Sebastian", "Designer")


# Named arguments
show_profile(job="Manager", name="Sebastian")
show_profile(job="Manager")


# Score function
def check_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Passed"
    else:
        return "Failed"

print(check_score(95))
print(check_score(85))
print(check_score(72))
print(check_score(65))


# Scope: global and local variables
name = "Sebastian"

def show_name():
    name = "Carlos"
    print(name)

show_name()
print(name)


# Another scope example
age = 27

def show_age():
    text = "Years old"
    print(age, text)

show_age()


# Final exercise
def calculate_total(price, quantity):
    total = price * quantity
    return total

print(calculate_total(10, 3))