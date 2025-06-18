s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"
b = s.split(",")
d = []
for part in b:
    part = part.strip().split(":")
    d.append(part[1].strip())
print(f"- {d[0]}\n- {d[1]}\n- {d[2]}")