from pydoc import text


def square(number):
    return(number * number)

def cube(number):
    return(number * number * number)

def is_positive(number):
    if number <= 0:
        return(False)
    else:
        return(True)

def is_even(number):
    if(number % 2 == 0):
        return(True)
    else:
        return(False)

def classify_number(number):
    if number > 0:
        return("Positive")
    elif number < 0:
        return("Negative")
    else:
        return("Zero")

def absolute_value(number):
    if number < 0:
        return(number * -1)
    else:
        return(number)

def max_of_two(a, b):
    if a > b:
        return(a)
    else:
        return(b)

def max_of_three(a, b, c):
    if a >= b and a >= c:
        return(a)
    elif b >= a and b >= c:
        return(b)
    else: 
        return(c)

def min_of_three(a, b, c):
    if a <= b and a <= c:
        return(a)
    elif b <= c and b <= a:
        return(b)
    else:
        return(c)

def absolute_value(number):
    if number < 0:
        return (number * -1)
    else:
        return(number)

def calculate_discount(price, discount):
    return(price - (discount / 100) * price )

def calculate_bill(bill, tip_porcentage):
    return bill + (tip_porcentage / 100) * bill

def calculate_total(price, discount, tip_porcentage):
    discounted_price = calculate_discount(price, discount)
    calculated_bill = calculate_bill(discounted_price, tip_porcentage)
    return calculated_bill

def calculate_average(a, b ,c):
    return (a + b + c) / 3

def is_adult(age):
    if age >= 18:
        return (True)
    else:
        return(False)

def classify_age(age):
    if age >= 18:
        return("Adult")
    elif age >= 13 and age <= 17 :
        return("Teenager")
    else:
        return("Child")

def calculate_grade(score):
    if score >= 90:
        return ("A")
    elif score >= 80:
        return("B")
    elif score >= 70:
        return("C")
    elif score >= 60:
        return("D")
    else:
        return("F")

def can_vote(age,  is_citizen):
    if age >= 18 and is_citizen: 
        return (True)
    else: 
        return(False)

def gets_discount(age, is_student):
    if age >= 65 or is_student:
        return(True) 
    else:
        return(False)

def can_enter_event(age, has_ticket):
    if age >= 18 and has_ticket:
        return(True)
    elif age >= 65:
        return(True)
    else:
        return(False)

def shipping_cost(total, is_member):
    if total >= 50 or is_member:
        return(0)
    else:
        return(7)

def final_price(price, is_member):
    discount = (10 / 100) * price
    if is_member:
        return(price - discount)
    else:
        return(price)

def apply_bonus(salary, years):
    bono = (10 / 100) * salary
    if years >= 5:
        return (salary + bono)
    else: 
        return salary 

def purchase_total(price, is_member, shipping):
    return 

def purchase_total(price, is_member, shipping):
    discount = (10 / 100) * price

    if is_member:
        return (price - discount) + shipping
    else:
        return price + shipping

def greet(name):
    return("Hello, " + name + "!")

def full_name(first_name, last_name):
    return(first_name + " " + last_name)

def name_length(name):
    return(len(name))

def is_long_name(name):
    if len(name) > 7:
        return(True)
    else:
        return(False)

def shout(text):
    return text.upper()

def normalize_name(name):
    return name.lower()

def remove_spaces(text):
    return text.strip()

def clean_text(text):
    return text.strip().lower()

def replace_spaces(text):
    return text.replace(" ", "-")

def format_username(name):
    return name.strip().lower().replace(" ", "_")