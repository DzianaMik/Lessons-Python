phrase = input("Введите фразу: ")
length = len(phrase)
words = len(phrase.split())
letters = "аеёиоуыэюя"
count_letters = sum(map(letters.__contains, phrase))
print("Количество символов:", length)
print("Количество слов:", words)
print("Количество гласных:", count_letters)
