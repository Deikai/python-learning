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
    report = {}
    
    report["average"] = average_grade(student)
    report["best_sub"] = best_subject(student)
    report["worst_sub"] = worst_subject(student)
    report["passed"] = passed_subjects(student, 13)

    return report 

def show_student_names(students):
    for student in students:
        print(student["name"])

def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

    return None

def student_average_by_name(students,name):
    student = find_student(students, name)
    if student is None:
        return None
    
    return average_grade(student)

def student_report_by_name(students, name):
    student = find_student(students, name)
    if student is None:
        return None
    
    return grade_report(student)

def best_student(students):
    best_average = None
    best_name = None

    for student in students:
        average = average_grade(student)
        if best_average is None or average > best_average:
            best_average = average
            best_name = student["name"]
    
    return best_name

