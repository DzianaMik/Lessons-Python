points = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
phrase = input("Ввести кодовою фразу из пяти символов используя только a, b, c, d: ")
total = sum(map(points.get, phrase))
print("Общее количество очков введенной фразы:", total)