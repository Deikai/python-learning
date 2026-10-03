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
