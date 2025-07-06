"""
Написать функцию print_n() которая будет печатать переданный текст, 
но при этом перед этим текстом выводить строку с номером отражающим 
кокай раз по счету выполняется эта функция. 

"""



counter = 0  
def print_n(text):
    global counter     
    counter += 1       
    print(f"{counter}: {text}")
print_n("Hello Python")

