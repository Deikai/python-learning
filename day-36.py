def say_python():
    print("I am learning Python")

def run_function(function):
    function()

run_function(say_python)
learning = say_python
learning()

def outer():
    def inner():
        print("Inside")
    
    return inner

function = outer()
function()

def create_greeting():
    def greeting():
        print("Hello Sebastian")
    
    return greeting

message = create_greeting()
message()

# def decorator(function):
#    def wrapper():
#        print("Before")

#        function()

#        print("After")
#    return wrapper

def add_messages(function):

    def wrapper(*args, **kwargs):
        print("Starting")

        result = function(*args, **kwargs)

        print("Finished")
        return result 
    return wrapper

new_function = add_messages(say_python)
new_function()

@add_messages
def study():
    print("Studying Python")

study()

@add_messages
def get_number():
    return 10

number = get_number()
print(number)

@add_messages
def welcome(name):
    print("Welcome " + name)

welcome("Sebastian")

@add_messages
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

from functools import wraps
def repeat(times):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            for number in range(times):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(4)
def study():
    print("Studying Python")

@repeat(3)
def greet(name):
    print("Hello ", + name)

greet("Sebastian")

@repeat(3)
def multiply(a, b):
    return(a * b)

result = multiply(4, 5)
print (result)

from functools import wraps
def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Running " + function.__name__)
        result = function(*args, **kwargs)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

result = add (5, 3)
print (result)

@log_call
def subtract(a, b):
    return a - b

result = subtract(10, 4)
print(result)

@log_call
@repeat(2)
def greet2(name):
    print("Hello " + name)