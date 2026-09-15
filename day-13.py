number = 1

while number <= 5:
    print(number)
    number = number + 2
# con este codigo la ultima linea es la que hace que el bucle se detenga, ya que cuando number es 5, la condicion number <= 5 ya no se cumple y el bucle termina.

for number in range(1, 6):
    print(number)
# con esta linea, el bucle for va a iterar desde 1 hasta 5, ya que range(1, 6) genera una secuencia de números del 1 al 5 (el 6 no está incluido).

for number in range(2, 11, 2):
    print(number)
# con esta linea, el bucle for va a iterar desde 2 hasta 10, incrementando de 2 en 2, ya que range(2, 11, 2) genera una secuencia de números del 2 al 10 (el 11 no está incluido) con un paso de 2.

for number in range(1, 6):
    print("Hello")
# con esta linea, el bucle for va a iterar desde 1 hasta 5, y en cada iteración va a imprimir "Hello".

for number in range(1, 6):
    print(number * 3)
# con esta linea, el bucle for va a iterar desde 1 hasta 5, y en cada iteración va a imprimir el resultado de multiplicar el número actual por 3.

for number in range(1, 10):
    if number == 5:
        break

    print(number)
# con esta linea, el bucle for va a iterar desde 1 hasta 9, pero cuando el número sea igual a 5, el bucle se detendrá y no se imprimirán los números 5, 6, 7, 8 y 9.

for number in range(1, 10):
    print(number)

    if number == 5:
        break
# con esta linea, el bucle for va a iterar desde 1 hasta 9, pero cuando el número sea igual a 5, el bucle se detendrá y no se imprimirán los números 6, 7, 8 y 9.

for number in range(1, 6):
    if number == 2:
        continue

print(number)
# con esta linea, el bucle for va a iterar desde 1 hasta 5, pero cuando el número sea igual a 2, se saltará la impresión de ese número y continuará con la siguiente iteración.

for number in range(1, 11):
    if number % 2 == 0:
        print(number)
# con esta linea, el bucle for va a iterar desde 1 hasta 10, y en cada iteración va a verificar si el número es par (es decir, si el residuo de dividirlo entre 2 es igual a 0). Si es par, se imprimirá el número.

for number in range(1, 11):
    if number % 2 != 0:
        print(number)
# con esta linea, el bucle for va a iterar desde 1 hasta 10, y en cada iteración va a verificar si el número es impar (es decir, si el residuo de dividirlo entre 2 no es igual a 0). Si es impar, se imprimirá el número.

for number in range(1, 11):
    if number % 2 != 0:
        print(number, "is odd")
    else:
        print(number, "is even")
# con esta linea, el bucle for va a iterar desde 1 hasta 10, y en cada iteración va a verificar si el número es impar o par. Si es impar, se imprimirá el número seguido de "is odd", y si es par, se imprimirá el número seguido de "is even".