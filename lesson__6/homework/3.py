'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''

number1 = int(input("Ввести число: "))
number2 = int(input("Ввести число: "))
number3 = int(input("Ввести число: "))
if number1 > number2 and number1 > number3:
    print("Наибольшее", number1)
elif number2 > number1 and number2 > number3:
    print("Наибольшее", number2)
else:
    print("Наибольшее", number3)