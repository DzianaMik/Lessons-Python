year = int(input("Введите ваш год рождения: "))
age = 2025 - year
if age < 0:
    print("Не родился")
if age <= 10:
    print("Ребёнок")
if age <= 17:
    print("Подросток")
if age <= 25:
    print("Юноша")
if age <= 45:
    print("В расцвете сил")
if age <= 65:
    print("Пожилой")
else:
    print("Старик")