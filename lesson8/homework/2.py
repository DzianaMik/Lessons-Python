'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''
def rectangle(a, b, operation="area"):
    if operation == "area":
        return a * b
    elif operation == "perimeter":
        return 2 * (a + b)
    else:
        return "Нет"