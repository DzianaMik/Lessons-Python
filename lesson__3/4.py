number = int(input("Введите число: "))
thousands = number // 1000
hundreds = (number % 1000) // 100
tens = (number % 100) // 10
units = number % 10
print(f"Тысячи: {thousands}")
print(f"Сотни: {hundreds}")
print(f"Десятки: {tens}")
print(f"Единицы: {units}")