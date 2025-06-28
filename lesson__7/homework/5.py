'''

Дан списк:
['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
Для каждого элемента в списке 
    - вывести на экран сначала номер элемента 
    - сам элемент 
    - символ данного элемента, соответствующий номеру его позиции в списке. 
Образец:
1 - qwertyu - q
2 - asdfggh - s
3 - zxcvbnm - c
и так далее...


'''


my_list = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
numb = 0
while numb < len(my_list):
    word = my_list[numb]
    if len(word) > numb:
        letter = word[numb]
    else:
        letter = "(no)"
    print(f"{numb + 1} - {word} - {letter}")
    numb += 1