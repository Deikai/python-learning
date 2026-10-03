fruits = ["apple", "banana", "orange"]
animals = ["dog", "cat", "bird", "fish"]
print(animals[1])

colors = ["red", "blue", "green", "yellow"]
colors[2] = "purple"

animals.append("horse")
colors.append("purple")

animals.remove("cat")
animals.remove("bird")
len(animals)
"cat" in animals 

def has_fruit(fruits, fruit):
    if fruit in fruits:
        return True
    else:
        return False

fruits.insert(1, "banana")

fruits.pop(1)

numbers = [10, 20, 30, 40]
removed_numbers = numbers.pop(2)

def total_prices(prices):
    return sum(prices)

numbers = [10, 50, 20, 5]
max(numbers)
min(numbers)

def highest_price(prices):
    return max(prices)

def analyze_prices(prices):
    highest = max(prices)
    lowest = min(prices)
    return highest - lowest
    