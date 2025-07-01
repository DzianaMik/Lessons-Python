def name(full_name, reverse = False):
    parts = full_name.split()
    if len(parts) != 3:
        return "Введите фамилию, имя и отчество"
    surname, name, patronymic = parts
    initials = f"{surname[0]}.{name[0]}.{patronymic[0]}."
    return initials
print(name("Михалевич Диана Анатольевна"))        
print(name("Михалевич Диана Анатольевна", True))

    

