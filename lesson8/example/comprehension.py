a = []
for i in range(1, 11):
    if i>5:
        a.append(i**2)
print(a)

b = [i**2 for i in range(1, 11)]
print(b)    
    
b = [i**2 for i in range(1, 11) if i < 5]
print(b)    

b = [i**2 if i<2 else 5 for i in range(1, 11) if i < 5]
print(b)    

b = [i**(2 if i<2 else 5) for i in range(1, 11) if i < 5]
print(b)    
    

users = [
    {"name":"Vasya1", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya2", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya3", "login":"vva@siiiia!",  "age":23},    
    {"name":"Vasya4asas", "login":"vvasiiiia",  "age":12},    
    {"name":"Vasya5", "login":"vvasiiiia!",  "age":23},    
    {"name":"Vasya6", "login":"vv#asiiiia",  "age":12},    
    {"name":"Vasya7", "login":"vvasiiiia",  "age":23},    
    {"name":"Vasya8", "login":"vvasiiiia!",  "age":23}
]    

a = [user for user in users if user['age'] < 16]
print(a)

a = [user for user in users if user['login'] == 'vva@siiiia!']
print(a)


b = [name.lower() for name in [user['name'] for user in users if user['age']==12]]
print(b)

# a = {key:val for user in users}
a = {'key-'+user['name']:user['age'] for user in users}
print(a)
a = {'key-'+user['name']:[user['age'], user['login']] for user in users}
print(a)

