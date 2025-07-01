text1 = input("Ввести строку: ").lower()
text2 = "аеиоуыэюя"
count = 0
for i in text1:
    if i in text2:
        count += 1
print(count)











  