"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""
a1 = 1.5
a2 = "Hello Python"
a3 = 3
a4 = 9.0
text1 = all(isinstance(i, float) for i in (a1, a2, a3, a4))
print(text1)
text2 = any(isinstance(i, str) for i in (a1, a2, a3, a4))
print(text2)
pair1 = isinstance(a1, int) and isinstance(a3, int)
pair2 = isinstance(a2, int) and isinstance(a4, int)
pair3 = isinstance(a3, int) and isinstance(a4, int)
print(pair1 or pair2 or pair3)
