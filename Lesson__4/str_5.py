name = input("Введите имя: ")
template = "Юзер с именем <имя> заходил на сайт в 15:00"
result = template.replace("<имя>", name)
print(result)