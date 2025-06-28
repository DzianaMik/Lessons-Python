'''
Запросить фразу состоящую минимум из трех слов. 
Сформировать фразу из этих слов в которой каждая буква слова, 
продублирована то количество раз, которое соответствует номеру позиции 
данной буквы в слове этой буквы. 
Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа

'''
phrase = input("Введите фразу из минимум трёх слов: ")
words = phrase.split()
if len(words) < 3:
    print("Введите минимум три слова.")
else:
    new = []
    for word in words:
        new_word = "" 
        for index, letter in enumerate(word, start=1):
            new_word += letter * index
        new.append(new_word)
    result = " ".join(new)
    print("Результат:", result)