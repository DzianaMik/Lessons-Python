text1 = int(input("Ввести число: "))
text2 = int(input("Ввести число: "))
text3 = int(input("Ввести число: "))
if text1 > text2 and text1 > text3:
    print("yes", text1)
if text2 > text1 and text2 > text3:
    print("no", text2)
else:
    print("Yes2", text3)