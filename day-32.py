class Employee:
    company = "OpenTech"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Ana", 70000)
employee2 = Employee("Carlos", 6000)

print(Employee.company)
print(employee1.company)
print(employee2.company)

