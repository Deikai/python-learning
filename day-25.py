student = {
    "name": "Sebastian",
    "age": 27,
    "grades": {
        "math": 13, 
        "english": 16,
        "python": 11
    }
}

def show_grades(student):
    for subject, grade in student["grades"].items():
        print(subject, grade)

def average_grade(student):
    count = 0
    average = 0
    for subject, grade in student["grades"].items():
        if type(grade) == int or type(grade) == float:
            count = count + 1
            average = average + grade

    if count == 0:
        return None

    average = average / count
    return average 

def best_subject(student):
    best_grade = None
    best_subject = None
    for subject, grade in student["grades"].items():
        if best_grade is None or grade > best_grade:
            best_subject = subject
            best_grade = grade

    return best_subject

def worst_subject(student):
    worst_sub = None
    worst_grade = None
    for subject, grade in student["grades"].items():
        if worst_grade is None or grade < worst_grade:
            worst_grade = grade
            worst_sub = subject

    return worst_sub

def passed_subjects(student, minimum):
    passed = []

    for subject, grade in student["grades"].items():
        if grade >= minimum:
            passed.append(subject)
    
    return passed

def grade_report(student):
    new = {}
    average = 0
    best_subject = 0
    worst_subject = 0
    passed = 0
    for subject, grade in student["grades"].item():
        return