count = 0
def greet_user(text):
    global count
    count += 1
    print(f"{count}: {text}")