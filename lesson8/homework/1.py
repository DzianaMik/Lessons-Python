"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def name(full_name, reverse = False):
    parts = full_name.split()
    if len(parts) != 3:
        return "Введите фамилию, имя и отчество"
    surname, name, patronymic = parts
    initials = f"{name[0]}.{patronymic[0]}."
    if reverse:
         return f"{initials}{surname}"
    else:
        return f"{surname} {initials}"
print(name("Михалевич Диана Анатольевна"))        
print(name("Михалевич Диана Анатольевна", True))
    