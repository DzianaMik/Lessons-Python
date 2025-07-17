# ООП


# абстракция
# наследование
# полиморфизм
# инкапсуляция


# ---------------------
# абстракция - берем все по минимуму только нужное




# -----------------
# наследования

# class Mixin1:
#     def f3(self):
#         print(3)

# class A:
#     a = 1
#     b = 2
#     e = 3
    
#     def __init__(self, val1):
#         print('aaa')
#         self.val1 = val1
    

#     def f1(self):
#         print(1)
    
# # class B:
# #     a = 1
# #     b = 2
# #     c = 3

# class E:
#     e = 5

#     def __init__(self):
#         print('eee')

# class B(A, Mixin1):    
#     c = 4    
#     def __init__(self, val1, val2):
#         # A.__init__(self, val1)        
#         super().__init__(val1)
#         self.val2 = val2
    
#     def f2(self):
#         print(2)
        


        
# class C(A, E, Mixin1):   
#    def __init__(self, val1):
#        A.__init__(self, val1)
#        E.__init__(self)
#        self.val3 = 0

        
# a = A(1)
# b = B(2, 3)        
# print(b.c)
# print(b.val1, b.val2)

# c = C(1)
# c.f3()


   
# from turtle import *

# class Turtle2(Turtle):
#     def __init__(self, shape = "turtle", color_='red', x=100, y=100):
#         super().__init__(shape=shape)
#         self.color(color_)
#         self.goto(x, y)
    
#     def goto100():
#         pass

        
# t = Turtle2(color_="blue", x=200, y=200)        
# mainloop()


# from typing import Any

# class List2(list):
   
#     def slice(self, n):
#         for i in range(n):
#             self.insert(0, self.pop())
            
            
#     # полиморфизм
# #   # переписали метод appepnd - теперь он вставляет не в конец а в начало       
#     def append(self, __object: Any) -> None:
#         # super().append(__object)
#         # super().append(__object)
#         self.insert(0, __object)
            
# a = List2()
# a += [1, 2, 3, 4, 5]
# a.append(6)
# # a.slice(1)
# print(a)
   
   
# ------------------------------------------
# инкапсуляция

# class User:
#     __age: int = 13 # private
#     _flag: bool = True    # protect - доступно через наследование

    
#     def __init__(self, age):
#         if not self.__check_age(age):
#             raise ...
#         self.__age = age
    
    
#     @staticmethod
#     def __check_age(age):
#         return age >= 14
    
#     @property #getter  
#     def age(self):        
#         print(11111)
#         return self.__age
    
#     @age.setter
#     def age(self, val):
#         if self.__check_age(val):
#             self.__age = val
#         else:
#             raise ValueError ("Возраст меньше 14")
    
    
#     def add_age(self):
#         self.age += 1
    
#     @property
#     def type(self):
#         return int(self._flag)
    
    

# user = User(22)

# # print(user.__age)   # ошибка т.к. __age приватная и ее имя изменено \
# #                       # механизмом name mangling и __age как бы не существует

# # user.__age = 12   # Python создаст новую переменную с именем __age в объекте user,
# # print(user.__age) # уже не выдает ошибку, т.к. в пред.строке мы ее создали (так делать нельзя)
# #                       


# user.age = 33 # проходит
# # user.age = 12 # не проходит проверку
# print(user.age)



# -----------------------------------------------
# # Утиная типизация 

# class A:
#     def foo1(self):
#         print(1)
#     def __len__(self):
#         return 1
    
# class B:
#     def foo1(self):
#         print(2)
#     def __len__(self):
#         return 2

# def f1(obj):
#     obj.foo1()
        
# a = A()
# b = B()

# f1(a)
# f1(b)

# l = [A(), B(), A(), "sas"]
# print(list(map(len, l)))
# for obj in l:
#     try:
#         obj.foo1()
#     except:
#         print('err')


# -----------------------------------------


# -----------------------------------------------       
# # абстрактные классы 
# # только для наследования
# from abc import ABC, abstractmethod

# class Basic(ABC):
#     __slots__ = ['a','b']
    
#     @abstractmethod # только для перезаписывания
#     def foo1(self):
#         print(1)


# class Child(Basic):    
#     def foo1(self): # должен быть обязательно
#         super().foo1()
#         print(2)
    
#     def f2(self):
#         print(3)

# # a = Basic()
# b = Child()
# # a.foo1()
# b.foo1()        
# b.f2()

# ----------------------------------------
# декораторы класса

# def class_decorator(cls):
#     attrs = dict(a=1, b=2, c=3)
#     for attr, val in attrs.items():
#         setattr(cls, attr, val) 
#     return cls

# @class_decorator
# class A:    
#     def a():
#         print(1)
        
        
# a = A()    
# print(a.a, a.b)	
# print(a.__dict__)


# ---------------------------------------------
# from dataclasses import dataclass
# from typing import Any

# # @dataclass(frozen=True)
# @dataclass
# class User:
#     # получаем упрощенную запись класса
#     # с реализованными методами __init__, __repr__, __str__ и __eq__
         
#     # аннотации типов обязательны
#     name:str
#     age:int
#     a: Any
    
# user = User('Alex', 33, 1)
# user.age = 20


# users = [
#     user,
#     User("Max", 20, '1'),
#     User("Djo", 20, True)
# ]

# print(user)
# # for user in users:
# #     print(user.age)
# #     # user.send_email()

# -------------------------------------------
# Метакласс — это класс, который управляет созданием и поведением других классов


# Метакласс — это класс для классов.
# Позволяет контролировать и изменять процесс создания классов.
# Используется для автоматизации, проверки и модификации классов при их определении.
# Создаётся путём наследования от type и переопределения методов __new__ и/или __init__.

# type - метакласc
# class A(type) - метакласc


# A = type("User", (), {'a':1, 'b':2})
# print(A)
# a = A()
# print(a)
# print(a.b)



# # --

# class UpperAttrMeta(type):
#     def __new__(cls, name, bases, attrs):
#         uppercase_attrs = {
#             key.upper() if not key.startswith('__') else key: val
#             for key, val in attrs.items()
#         } 
#         return super().__new__(cls, name, bases, uppercase_attrs)

# class SimpleClass(metaclass=UpperAttrMeta):
#     attr1 = "value1"
#     attr2 = "value2"

# print(hasattr(SimpleClass, 'attr1'))  # False
# print(hasattr(SimpleClass, 'ATTR1'))  # True



# print('-'*20)

# # перехват инит
# class Meta(type):
#     def __init__(cls, name, bases, attrs):
#         print(f"Инициализация класса {name} метаклассом")
#         super().__init__(name, bases, attrs)
#         cls.custom_attr = "Добавлено метаклассом"

# class MyClass(metaclass=Meta):
#     def __init__(self, value):
#         print(f"Инициализация экземпляра MyClass с value = {value}")
#         self.value = value

# # Создание экземпляра класса
# obj = MyClass(42)
# print(obj.value)          # 42
# print(obj.custom_attr)  # Добавлено метаклассом
# print(obj.__dict__)


# добавление атрибута не в класс а в объект
class Meta(type):
    def __new__(cls, name, bases, attrs):
        # Сохраняем оригинальный __init__, если он есть
        original_init = attrs.get('__init__')

        # Определяем новый __init__
        def __init__(self, *args, **kwargs):
            # Добавляем атрибут в экземпляр
            self.meta_attr = 'Добавлено метаклассом'
            # Вызываем оригинальный __init__, если он был
            if original_init:
                original_init(self, *args, **kwargs)

        # Заменяем __init__ в атрибутах класса
        attrs['__init__'] = __init__

        # Создаём класс с изменёнными атрибутами
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value

obj = MyClass(10)
print(obj.value)      # 10
print(obj.meta_attr)  # Добавлено метаклассом
print(obj.__dict__)
