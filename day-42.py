def calculate_price(price: float, quantity: int) -> float:
    total_price = (price * quantity)
    return total_price

def is_adult(age: int) -> bool:
    if age >= 18:
        return True
    return False

def show_name(name:str) -> None:
    print(name)

names: list[str] = ["sebastian", "Ana", "Pedro"]

def show_names(names: list[str]) -> None:
    for name in names:
        print(name)

people: dict[str, int] = {
    "sebastian": 27,
    "Ana": 25
}

def get_age(people: dict[str, int], name: str) -> int:
    return people[name]

languages = ["Python", "JavaScript", "Java"]

def find_language(languages: list[str], search:str)-> str|None:
    for language in languages:
        if language == search:
            return(language)
    return None

scores = [
    {"Python": 95},
    {"JavaScript": 80},
    {"Java": 75}
]

def show_scores(scores: list[dict[str, int]])-> None:
    for score in scores:
        print(score)

coordinates = (39.10, -94.58)

def show_coordinates(coordinates:tuple[float, float])-> None:
    print(coordinates)

languages = {"Python", "JavaScript", "Java"}

def show_unique_languages(languages:set[str])-> None:
    for language in languages:
        print(language)

products: dict[str, float] = {
    "Mouse": 25.0,
    "Keyboard": 70.0,
    "Monitor": 180.0
}

def find_price(products: dict[str, float], product_name: str)-> float|None:
    if product_name in products:
        return products[product_name]
    return None

print(find_price(products, product_name="Mouse"))

products: dict[str, float] = {
    "Mouse": 25.0,
    "Keyboard": 70.0,
    "Monitor": 180.0
}

cart: list[str] = ["Mouse", "Keyboard"]

def calculate_total(products:dict[str, float], cart: list[str])-> float:
    total = 0.0
    for product in cart:
        if product in products:
            total = products[product] + total
    return total

print(calculate_total(products, cart))