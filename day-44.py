from dataclasses import dataclass

def show_role(role: str)-> None:
    match role:
        case "admin":
            print("Full access")
        case "editor":
            print("Edit access")
        case "user":
            print("Basic access")
        case _:
            print("Unknown role")

def show_http_status(status: int)-> None:
    match status:
        case 200|201:
            print("Success")
        case 400|404:
            print("Client error")
        case 500|503:
            print("Server error")
        case _:
            print("Unknown status")

def describe_point(point: tuple[int, int])-> None:
    match point:
        case (0,0):
            print("Origin")
        case (x,0):
            print("X axis:", x)
        case (0,y):
            print("Y axis:", y)
        case (x,y):
            print("Point:", x, y)

def describe_number(number: int)-> None:
    match number:
        case number if number > 0:
            print("Positive")
        case number if number < 0:
            print("Negative")
        case 0:
            print("Zero")

def describe_user(user: dict[str, str])-> None:
    match user:
        case {"name": name, "role": "admin"}:
            print("Admin:", name)
        case {"name": name, "role": "user"}:
            print("User:", name)
        case _:
            print("Unknown user")

def describe_list(numbers: list[int])-> None:
    match numbers:
        case [x]:
            print("One:", x)
        case [x, y]:
            print("Two:", x, y)
        case [x, y, z]:
            print("Three:", x, y, z)
        case _:
            print("Other list")

def split_values(values: list[int])-> None:
    match values:
        case []:
            print("Empty")
        case [first]:
            print("Only:", first)
        case [first, *rest]:
            print("First:", first, "Rest:", rest)

@dataclass
class Product:
    name: str
    category: str

def describe_product(product: Product) -> None:
    match product:
        case Product(name, "tech"):
            print("Tech:", name)
        case Product(name, "food"):
            print("Food:", name)
        case Product():
            print("Other product")

def process_event(event: dict)-> None:
    match event:
        case {"type": "login", "user": name}:
            print("Login:", name)
        case {"type": "message", "data": [sender, message]}:
            print("From:", sender)
            print("Message:", message)
        case {"type": "location", "coordinates": (x,y)}:
            print("Location:", x, y)
        case _:
            print("Unknown event")

def process_order(order: dict)-> None:
    match order:
        case {"status": "pending"}:
            print("Order pending")
        case {"status": "paid", "total": total} if total >= 100:
            print("Large order:", total)
        case {"status": "paid", "total": total}:
            print("Paid order:", total)
        case {"status": "cancelled"}:
            print("Order cancelled")
        case _:
            print("Unknown order")
