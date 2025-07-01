a = 10

def print10():
   for i in range(10):
        print('hello')


def print_n(text: str, n: int=3, flag=True, param:dict = {"sep":" "}): # параметры
    '''
    Выводит на печать text n количество раз
    '''
    
    val1 = param.get('key1')
    if val1:
        pass # делаем что-то только тогда когда в param есть ключ key1
    
    n = int(n)
    # b = 1
    for i in range(n):
        print(text, sep=param['sep'])
    

def s1(a:int, b:int) -> int: 
    # ss = a*b      
    # return ss
    return a*b
    
def s2(a:int, b:int) -> tuple[int|str]:    
    err = ''
    s1 = 0
    if isinstance(a, int) and isinstance(b, int):
        s1 = a * b
    else:
        err = 'err - очень хочется int'
    
    a, b = 1, 2 # для примера того что можно возвращать много значений
    return s1, err, a, b

def s3(a:int, b:int) -> tuple[int|str]:        
    if isinstance(a, int) and isinstance(b, int):
        return a * b # return завершает функцию
    
    # т.к. в if есть return который завершит функцию else можно не писать
    # сюда дойдет только если if не сработает
    raise ValueError("Только int")
    

   

   
print(123)

# print10()
# print_n("Python", "10") # аргументы

# print(len('Hello'))
# a = len('Hello')

print(s1(4, 5)) # позиционные
s = s1(a=4, b=5) # именованные
print(s)

s = s2(b=5, a=3) # вернет кортеж
print(s)

s, err1, a, b1  = s2(4, "5") # распаковка 
print(s or err1)

try:
    s = s3(4, "5")
except Exception as e:
    print(f"---err---\n{e}")
else:
    print(s)
          
    
    
    




print('------------')
    

def max_n(a, b):    
    return a if a>b else b

#найти наибольшее из трех
a1, a2, a3 = 5, 4, 2
print(max_n(max_n(a1, a2), a3))    

    