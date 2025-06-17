phrase = input("Введите фразу: ")
length = len(phrase)
words = len(phrase.split())
vowels = "добрыйдень"
count_vowels = sum(map(vowels.__contains__, phrase))
print("Количество символов:", length)
print("Количество слов:", words)
print("Количество гласных:", count_vowels)
