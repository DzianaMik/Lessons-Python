'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
data = [True, "text", 123, False, None, "another", 0]
text1 = list(filter(lambda x: isinstance(x, str), data))
text2 = list(filter(lambda x: type(x) == bool, data))
print(text1)
print(text2)