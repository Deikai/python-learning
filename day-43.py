from dataclasses import dataclass, field, asdict

@dataclass
class Student:
    name: str
    age: int
    course: str

student =  Student("Sebastian", 27, "Python")

print(student)
print(student.name)

@dataclass
class Course:
    name: str
    duration: int
    active: bool = True

course = Course("Python", 8)

print(course)
print(course.active)

@dataclass
class Employee:
    name: str
    salary: float
    department: str = "General"
    active: bool = True

employee = Employee("Ana", 50000.0)
print(employee)

@dataclass
class Project:
    name: str
    completed: bool = False
    tasks: list[str] = field(default_factory=list)

    def add_task(self, task: str)-> None:
        self.tasks.append(task)

project = Project("Portfolio")
print(project)
print(project.tasks)

project_data = asdict(project)
print(project_data)
print(project_data["name"])

project.add_task("Create homepage")
project.add_task("Add contact form")

print(project.tasks)

@dataclass
class Book:
    title: str
    author: str
    pages:int

book1 = Book("1984", "George Orwell", 328)
book2 = Book("1984", "George Orwell", 328)
book3 = Book("Dune", "Frank Herbert", 412)

print(book1 == book2)
print(book1 == book3)

@dataclass (frozen=True)
class Coordinates:
    latitude: float
    Longitude: float

location = Coordinates(39.10, -94.58)

print(location)

@dataclass(order=True)
class Player:
    score: int
    name: str

player1 = Player(80, "Sebastian")
player2 = Player(95, "Ana")

print(player1 < player2)
print(player1 > player2)

@dataclass
class Account:
    name: str
    balance: float

    def __post_init__(self):
        if self.balance < 0:
            self.balance = 0.0

account = Account("Sebastian", -100.0)
print(account)

@dataclass
class InventoryItem:
    name: str
    price: float
    quantity: int = 0
    tags: list[str] = field(default_factory=list)

    def __post_init__(self):
        if self.price < 0:
            self.price = 0.0
        if self.quantity < 0:
            self.quantity = 0

    def total_value(self,) -> float:
        total = self.price * self.quantity
        return total

item = InventoryItem("Keyboard", 70.0, 3)
print(item)
print(item.total_value())