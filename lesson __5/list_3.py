name = []
name.append(input("Ввести имя: "))
name.append(input("Ввести имя: "))
name.append(input("Ввести имя: "))
name.append(input("Ввести имя: "))
name.append(input("Ввести имя: "))
name[0], name[-1] = name [-1], name [0]
remove = name.pop(2)
print("Список:", name)
print("Удаленный элемент:", remove)