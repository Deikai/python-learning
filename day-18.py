try:
    numero = int(input("dime un numero: "))
    if numero % 2 != 0:
        print("Odd")
    else:
        print("Even")

except ValueError:
    print("Invalid number")

finally:
    print("Finished")


try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Invalid age")
    elif age <= 12:
        print("Child")
    elif age <= 17:
        print("teenager")
    else:
        print("Adult")

except ValueError:
    print("Invalid age")
finally:
    print("Finished")


import math

print(math.sqrt(25))
# calcula la raiz cuadrada de 25

print(math.sqrt(49))

from math import sqrt  # esta es otra forma de importar la sqrt desde math

valor = int(input("Ingresa un numero: "))
result = float(valor)
print(sqrt(result))

try:
    valor = float(input("Ingresa un numero: "))
    print(sqrt(valor))
except ValueError:
    print("Please enter a valid number")
finally:
    print("Program finished")

import math
try:
    valor = float(input("Enter a number: "))
    if valor < 0:
        print("Negative numbers are not allowed.")
    else:
        print(math.sqrt(valor))
except ValueError:
    print("Please enter a valid number")
finally:
    print("Program finished")

math.ceil(7.8)   # 8
math.floor(7.8)  # 7
# # ceil redondea hacia arriba y floor hacia abajo

try:
    valor = float(input("Ingresa un valor: "))
    print(math.ceil(valor))
    print(math.floor(valor))
except ValueError:
    print("Ingresa un valor valido. ")


try:
    valor = float(input("ingresa un valor decimal: "))
    if valor < 0:
        print("Negative number are not allowed ")
    else:
        print(math.ceil(valor))
        print(math.floor(valor))
        print(math.sqrt(valor))
except ValueError:
    print("Please enter a valid number.")


try:
    valor = float(input("ingresa un valor decimal: "))
    if valor < 0:
        print("Negative numbers are not allowed.")
    else:
        print(math.sqrt(valor))
        print(math.ceil(valor))
        print(math.floor(valor))
        print(math.pi)
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Program finished.")