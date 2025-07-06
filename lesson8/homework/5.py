'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''


def count_char(text):
    result = {}
    for i in text:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

print(count_char("hello"))

