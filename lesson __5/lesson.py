grades = {
    "Анна": 5,
    "Борис": 4,
    "Вика": 3,
    "Гена": 5,
    "Даша": 4
}
for student, grade in grades:
    student, grade = grades.items()
    print(f"{student} - {grade}")
