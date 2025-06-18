phrase = input("Введите фразу: ")
length = len(phrase)
words = len(phrase.split())
letters = "аеёиоуыэюяeyuo"
count_letters = sum(map(letters.__contains__, phrase))
print("Количество символов:", length)
print("Количество слов:", words)
print("Количество гласных:", count_letters)
