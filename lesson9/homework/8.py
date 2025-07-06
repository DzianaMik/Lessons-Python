'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
data = [True, "text", 123, False, None, "another", 0]
date1 = list(filter(lambda x: isinstance(x, str), lst))
date2 = list(filter(lambda x: type(x) == bool, lst))
print(date1)
print(date2)