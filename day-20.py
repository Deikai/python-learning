
from operations import square, cube, is_positive, is_even, classify_number, absolute_value
try: 
    number = float(input("Ingrese un valor: ")) 
    print(square(number))
    print(cube(number))
    print(is_positive(number))
    print(is_even(number))
    print(classify_number(number))
    print(absolute_value(number))
except ValueError:
    print("Ingrese un valor valido. ")



