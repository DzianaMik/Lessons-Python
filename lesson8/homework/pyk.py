def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
num = int(input("Введите число: "))
if is_even(num):
    print(f"Число {num} — чётное.")
else:
    print(f"Число {num} — нечётное.")
   

    

