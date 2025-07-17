import enum

# Определяем перечисление статусов багов
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

# Доступ к имени и значению
print(f"Имя статуса: {BugStatus.wont_fix.name}")
print(f"Значение статуса: {BugStatus.wont_fix.value}")

# Перебор всех статусов
print("\nВсе статусы багов:")
for status in BugStatus:
    print(f"{status.name} = {status.value}")
