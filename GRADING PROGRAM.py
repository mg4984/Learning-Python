student_scores= {
    "mohit" :100,
    "kamakshi" :92,
    "prissa" :90,
    "yuvraj" :88
}
student_grades = {}

for student in student_scores:
    scores=student_scores[student]
    print(scores)
    if scores>90:
        student_grades[student] = "Outstanding"    
    elif scores>80:
        student_grades[student] = "excellent"
    elif scores>70:
        student_grades[student] = "average"
    else:
        student_grades[student] = "Fail"
print(student_grades)