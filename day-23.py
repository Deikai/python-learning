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


numbers = [4, 7, 10, 13, 18]
for number in numbers:
    if number == 10:
        print("found")
        break


def contains_number(numbers, target):
    for number in numbers:
        if target == number:
            return True

    return False

numbers = [1, 2, 3, 4, 5, 6]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

def positive_numbers(numbers):
    positive = []
    for number in numbers:
        if number <= 0:
            continue
        positive.append(number)

    return positive

def first_greater(numbers, limit):
    for number in numbers:
        if number > limit:
            return number

    return None

def first_long_word(words, min_lenght):
    for word in words:
        if len(word) > min_lenght:
            return word
    
    return None

def first_starts_with(words, letter):
    for word in words:
        if word.startswith(letter):
            return word
    
    return None

def count_long_words(words, min_lenght):
    count = 0
    for word in words:
        if len(word) > min_lenght:
            count = count + 1
    
    return count

def count_starts_with(words, letter):
    count = 0
    for word in words:
        if word.startswith(letter):
            count = count + 1
    
    return count

def word_starting_with(words, letter):
    starts = []
    for word in words:
        if word.startswith(letter):
            starts.append(word)
    
    return starts

def even_greater_than(numbers, limit):
    even = []
    for number in numbers:
        if number % 2 == 0 and number > limit:
            even.append(number)
    
    return even

def sum_greater_than(numbers, limit):
    count = 0
    for number in numbers:
        if number > limit: 
            count = number + count

    return count

def average_greater_than(numbers, limit):
    sum = 0
    count = 0
    for number in numbers:
        if number > limit:
            sum = number + sum
            count = count + 1
    if count == 0:
        return None

    average = sum / count     

    return average

def average_even(numbers):
    sum = 0
    count = 0
    for number in numbers:
        if number % 2 == 0:
            sum = sum + number
            count = count + 1

    if count == 0:
        return None

    average = sum / count 
    return average

def longest_word(words):
    longest = words[0]
    if len(word) == 0:
        return None

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest

def largest_number(numbers):
    if len(numbers) == 0:
        return None
    largest = numbers[0]


    for number in numbers:
        if number > largest:
            largest = number

    return largest

def smallest_number(numbers):
    if len(numbers) == 0:
        return None
    smallest = number [0]
    
    for number in numbers:
        if number < smallest:
            smallest = number
        
    return smallest

def min_max(numbers):

    if len(numbers) == 0:
        return None
    minor = numbers[0]
    bigger = numbers[0]

    for number in numbers:
        if number > bigger:
            bigger = number

    for number in numbers:
        if number < minor:
            minor = number
    
    return [minor, bigger]

def min_max2(numbers):
    if len(numbers) == 0:
        return None
    
    bigger = numbers[0]
    minor = numbers[0]
    for number in numbers:
        if number > bigger:
            bigger = number
        
        if number < minor:
            minor = number

    return [minor, bigger]

def count_occurrences(items, target):
    count = 0
    for item in items:
        if target == item:
            count = count + 1
    return count 

def remove_target(items, target):
    new_list = []
    for item in items:
        if item == target:
            continue
        new_list.append(item)
    return new_list

def replace_target(items, target, replacement):
    new_list = []
    for item in items:
        if target == item:
            item = replacement
        new_list.append(item)
    return new_list

def double_numbers(numbers):
    new = []
    for number in numbers:
        number = number * 2
        new.append(number)
    return new

def analyze_numbers(numbers):
    if len(numbers) == 0:
        return None
    cantidad_pares = 0
    suma_pares = 0
    menor = numbers[0]
    mayor = numbers[0]
    
    for number in numbers:
        if number % 2 == 0:
            cantidad_pares = cantidad_pares + 1
            suma_pares = suma_pares + number

        if number > mayor:
            mayor = number

        if number < menor:
            menor = number

    return [cantidad_pares, suma_pares, menor, mayor]