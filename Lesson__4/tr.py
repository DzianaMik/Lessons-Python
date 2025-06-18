b = "Hello Python"
print(b.lower())

с = "Python Hello Hello"
print(b.lower())



a = 42
b = "Привет"
c = 3.14
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"
b = s.split(",")
d = []
for part in b:
    part = part.strip().split(":")
    d.append(part[1].strip())
print(f"- {d[0]}\n- {d[1]}\n- {d[2]}")

info = "название: Война и мир, автор: Лев Толстой, год: 1869"
value = info.split(",")
date = []
for part in value:
    part = part.strip().split(":")
    date.append(part[1].strip())
print(f"{date[0]}\n- {date[1]}\n- {date[2]}")