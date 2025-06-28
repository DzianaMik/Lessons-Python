total = 0
count = 0
while True:
    text = int(input("Ввести число: "))
    if text == 0:
        break
    total += text
    count += 1
print(f"Сумма чисел: {total}")
print(f"Количество чисел: {count}")