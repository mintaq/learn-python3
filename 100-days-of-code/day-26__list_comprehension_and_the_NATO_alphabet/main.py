import random

names = ["Thu", "Minh", "Soc", "Mom", "Dad"]
student_scores = {student: random.randint(1, 10) for student in names}
passed_students = {student: score for (student, score) in student_scores.items() if score > 5}
print(student_scores)
print(passed_students)
