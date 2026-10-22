class Employee:
    company = "OpenTech"
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count = Employee.employee_count + 1

    def give_raise(self, amount):
        self.salary  = self.salary + amount

    def info(self):
        return (self.name, self.salary, self.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company =  new_company

    @staticmethod
    def is_high_salary(salary):
        if salary >= 60000:
            return True
        else: 
            return False

employee1 = Employee("Ana", 70000)
employee2 = Employee("Carlos", 6000)

Employee.change_company("CodeWorks")

print(Employee.company)
print(employee1.company)
print(employee2.company)
print(Employee.employee_count)
employee1.give_raise(5000)
print(employee1.salary)
print(Employee.is_high_salary(employee1.salary))
print(employee1.info())