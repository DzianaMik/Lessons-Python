d = {'one':11, 'two':22, 'hello':'python', True:False}
keys = list(d)
n = int(input("Введите номер элемента: "))
del d[keys[n]]
print(d)