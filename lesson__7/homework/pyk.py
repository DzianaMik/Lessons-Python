total = 0
count = 0
while True:
    text = int(input("Oki"))
    if text == 0:
        break
    total += text
    count += 1
if count > 0:
    maximum = max(total)
    print(f"Максимальное: {maximum}")
else:
    print("Ошибка")

  