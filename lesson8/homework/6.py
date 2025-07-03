"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
def yes_or_n(full_number):
     if not all(isinstance(x, int) for x in full_number):
        return False
     seen = set()    
     result = []
     for num in full_number:
        if num in seen:
            result.append("Yes")
        else:
            result.append("No")
            seen.add(num)
     return result
