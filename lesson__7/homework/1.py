"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""
total = 0
count = 0
while True:
    grades = int(input("Ввести оценки: "))
    if grades == 0:
        break
    total += grades
    count += 1
if count > 0:
    average = total / count
    print(f"Средний балл ученика: {average}")
else:
    print("Ошибка")

