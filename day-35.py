class Playlist:
    def __init__(self, songs):
        self.songs = songs
    
    def __iter__(self):
        return iter(self.songs)
    
    def __next__(self, current):
        if self.current > 3:
            return StopIteration

songs = ["Song A", "Song B", "Song C"]
playlist1 = Playlist(songs)

for song in playlist1:
    print(song)

iterator = iter(["Python", "HTML", "JavaScript"])
next(iterator)
next(iterator)
next(iterator)
next(iterator)

class Counter:
    def __init__(self):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.end:
            new = self.current
            self.current = self.current + 1
            return new
        raise StopIteration

counter1 = Counter(3, 6)
for number in counter1:
    print(number)

def languages():
    yield "Python"
    yield "HTML"
    yield "JavaScript"

for language in languages():
    print(language)

def numbers():
    for number in range(1, 4):
        yield number

def count_up_to(end):
    for number in range(1, end + 1):
        yield number

def even_numbers(end):
    for number in range(1, end + 1):
        if number %2 == 0:
            yield number 

generator = even_numbers(8)


def expensive_product(products, minimum):
    for product in products:
        if product.price >= minimum:
            yield product


product1 = Product("Keyboard", 50)
product2 = Product("Monitor", 200)
product3 = Product("Mouse", 25)
products = [product1, product2, product3]

for product in expensive_product(products, 50):
    print(product.name)

def expensive_product_names(products, minimum):
    for product in products:
        if product.price >= minimum:
            yield product.name

for name in expensive_product_names(products, 50):
    print(name)

def discounted_prices(products, discount):
    for product in products:
        yield product 