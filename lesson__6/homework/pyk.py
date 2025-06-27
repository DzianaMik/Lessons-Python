text1 = input("Ввести число: ")
text2 = input("Ввести число: ")
text3 = int(input("Ввести число: "))
if text1 == "admin" and text2 == 123456:
    print("Разрешено")
elif text1 == "vasya" and text2 == "vas123" and text3 < 60:
    print("Разрешено")
else:
    print("Запрещено")
