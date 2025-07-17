"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""
def check(x):
    count = 0  
    for char in x:
        if char == '(':
            count += 1  
        elif char == ')':
            count -= 1  
            if count < 0:
                return False

    return count == 0


