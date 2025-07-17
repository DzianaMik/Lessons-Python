
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
    
    
    def print_info(self, flag = True):
        if flag:
            print('--------------')    
        print(f"Имя - {self.name} - {self.age}")
    
    def calc_bd2(self):
        return 2025-self.age
    
print("111111")