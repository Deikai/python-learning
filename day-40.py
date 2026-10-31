import csv

with open("students.csv", "r") as file:
    students = csv.reader(file)
    for student in students:
        print(student)

with open("students.csv", "r") as file:
    students = csv.DictReader(file)
    for student in students:
        print(student["name"])

with open("languages.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["language", "level"])
    writer.writerow(["Python", "Intermdiate"])
    writer.writerow(["JavaScript", "Basic"])
    writer.writerow(["HTML", "Intermediate"])

employees = [
    ["Ana", 45000]
    ["Luis", 60000]
    ["Marta", 52000]
]
