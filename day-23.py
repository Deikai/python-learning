animals = ["dog", "cat", "bird", "fish"]
for animal in animals:
    print(animal)

numbers = [2, 4, 6, 8]
for number in numbers:
    print(number * 2)

numbers = [1, 2, 3, 4]
doubled = []
for number in numbers:
    doubled.append(number * 2)

numbers = [3, 5, 7]
squared = []
for number in numbers:
    squared.append(number * number)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

numbers = [3, 8, 1, 10, 5, 12]
greater_than_five = []
for number in numbers:
    if number > 5:
        greater_than_five.append(number)

numbers = [2, 4, 6, 7, 8, 11, 12]
result = []
for number in numbers:
    if number > 5 and number % 2 == 0:
        result.append(number)

numbers = [2, 3, 4, 5, 6, 7, 8]
count = 0
for number in numbers:
    if number % 2 == 0:
        count = (count + 1)

numbers = [5, 12, 3, 20, 8, 1, 15]
count = 0
for number in numbers:
    if number > 10:
        count = count + 1

numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
    total = total + number

numbers = [1, 2, 3, 4, 5, 6]
total = 0
for number in numbers:
    if number % 2 == 0:
        total = total + number

numbers = [3, 7, 2, 9, 4]
total = 0
for number in numbers:
    if number > 4:
        total = total + number

numbers = [2, 5, 8, 11, 14, 3]
total = 0
count = 0
for number in numbers:
    if number % 2 == 0:
        count = count + 1
        total = total + number

def count_even(numbers):
    count_even = 0
    for number in numbers:
        if number % 2 == 0:
            count_even = count_even + 1

    return count_even

def sum_even(numbers):
    sum_even = 0
    for number in numbers:
        if number % 2 == 0:
            sum_even = sum_even + number 
    
    return sum_even

def greater_than(numbers, limit):
    greater_than_seven = []
    for number in numbers:
        if number > limit:
            greater_than_seven.append(number)
    return greater_than_seven
    
