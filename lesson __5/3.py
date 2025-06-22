d = {'one':11, 'two':22, 'hello':'python', True:False}
key = list(d)
number = int(input("Введите номер элемента: "))
del d[key[number]]
print(d)