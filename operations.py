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

