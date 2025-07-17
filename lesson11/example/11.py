#ООП
    # - свойства (атрибуты, поля)
    # - методы (действия)
    
# class A:
#     pass

# a1 = A()
# a2 = A()
# a3 = A()

# print(a1)




class User:
    # login: str = 'a123' # атрибут класса
    password: str = "*"
    count_ = 0
    
    @classmethod
    def change_pas(cls, val):
        cls.password = val
    
        
    @staticmethod #служебный метод
    def calc_bd(val: int):
        return 2025-val
        
    
    def __init__(self, age, name1):
        self.age = age # атрибуты объекта
        self.name = name1
        self.login = ""
        
    def __str__(self): # для людей
        return f"Имя - {self.name} - {self.age}"
    
    # если нет __str__ принт использует __repr__
    def __repr__(self): # для машин
        return f"User({self.age}, '{self.name}')"
    
    def __eq__(self, other_obj):
        return self.name == other_obj.name
    
    def __lt__(self, other_obj):
        return self.age < other_obj.age
    
    # аналогично
    # __ne__(self, other)   obj1 != obj2
    # __le__(self, other)   obj1 <= obj2
    # __gt__(self, other)   obj1 >  obj2
    # __ge__(self, other)   obj1 >= obj2
    
    def __call__(self, *args, **kwds):
        print(f"Я {self.name}")
    
    def print_info(self, flag = True):
        if flag:
            print('--------------')    
        print(f"Имя - {self.name} - {self.age}")
    
    def calc_bd2(self):
        return 2025-self.age
    

class Users:
    def __init__(self, n=0):
        self.users = []
        self.n = n

    def add(self, user:User):
        self.users.append(user)
        
    def __len__(self):
        return len(self.users)

    def __getitem__(self, val): #obj[0]
        
        return self.users[val]
    
    def __setitem__(self, key, value):
        self.users[key] = value
        
    def __iter__(self):        
        return iter(self.users)

    def __next__(self):
        if self.n >= len(self.users):
            raise StopIteration
        res =  self.users[self.n]
        self.n+=1
        return res


user = {
    'age':55,
    'name1':"name1"
}    
    

user1 = User(age=33, name1='Max')
        
user2 = User(22, 'Max')
User.change_pas('1234')
user1.__class__.password = '12345'
user3 = User(44, 'Petya2')
user4 = User(**user)
user4.password = '1111'



print(user1.login)
print(user1.__dict__)
user1.login = "login123"
print(user1.__dict__)
print(user2.__dict__)
print(user1.name, user1.login, user1.password)
print(user2.name, user2.login, user2.password)
print(user3.name, user3.login, user3.password)
print(user4.name, user4.login, user4.password)

user4.print_info()
user3.print_info(flag=False)

users = [user1, user2, user3, user4]

print(111, user1)
print(*users, sep='\n')
print(repr(user1))

users = Users()
users.add(user1)
users.add(user2)
users.add(user3)
print(users)

print(len(users)) 

print(users[2]) # getitem
users[2] = user2 # setitem
print(users[2])


# user1.name
a = "name"
a = "age"
getattr(user1, a)
setattr(user1, a, 55)
# delattr()

# user.age


for user in users:
    print(user)

# list(users)
    
print(user1 == user2) # __eq__
print(user2 < user1) # __lt__

users.users.sort(reverse=True)

print(*users, sep='\n')

try:
    print("next", next(users)) # __next__
    print("next", next(users)) # __next__
    print("next", next(users)) # __next__
    print("next", next(users)) # __next__
except StopIteration:
    print('больше нет')



user1() # __call__

# -------------------------------------------------
# import time

# print(time.localtime())
# print(time.localtime().tm_year)



# ---------------------------- Менеджер контекста
# class A:
#     def __init__(self):
#         self.con = 1
    
    
#     def __enter__(self): # срабатывает при создании объекта с помощью with
#         print(1111)
#         return self.con
        
#     def __exit__(self, q, w, e): # срабатывает когда with закончился
#         self.con=0
#         print(2222)
    
    
# # a = A()
# # print(333)
# # a.con=0
        
# with A() as a:
#     print(a)
#     print(333)


# ---------------------------------------
users2 = [
    User(22, 'qqq'),
    User(33, 'ww'),
    User(22, 'eee'),
]

for i, user in enumerate(users2):
    print(f"for{i}", user.name, user.password)