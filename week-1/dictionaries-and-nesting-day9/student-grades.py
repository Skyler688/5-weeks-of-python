# python3 week-1/dictionaries-and-nesting-day9/student-grades.py

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    
    score = student_scores[student]
    grade = "Fail"
    
    if (score > 90):
        grade = "Outstanding" 
    elif (score > 80):
        grade = "Exceeds Expectations"
    elif (score > 70):
        grade = "Acceptable"
    
    student_grades[student] = grade

print(student_grades)