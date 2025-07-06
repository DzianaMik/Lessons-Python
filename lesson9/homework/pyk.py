items = [10, "apple", True, 5, "banana", False, 3.14, "cherry"]
text1 = list(filter(lambda x: isinstance(x, (int, float)), items))
text2 = list(filter(lambda x: isinstance(x, str), items))
print(text1)
print(text2)
