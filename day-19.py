import math 
try:
    valor = float(input("Ingresa un valor decimal: "))
    if valor < 0:
        print("Negative number")
    else:
        print(math.ceil(valor))
        print(math.floor(valor))
except ValueError:
    print("Ingrese un numero valido.")
finally:
    print("Program finished")


import calculator
print(calculator.add(5, 3))

print(calculator.subtract(9, 4))

print(calculator.multiply(10, 2))

print(calculator.divide(10, 2))

from calculator import multiply
print(multiply(6, 4))

from calculator import add, divide
print(add(20, 5))
print(divide(100, 4))

from messages import greet, goodbye
print(greet("Sebastian"))
print(goodbye("Sebastian"))
