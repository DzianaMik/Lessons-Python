"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""
import re
from datetime import date

class User:
    def __init__(self, name, login, password, subscription_date, subscription_mode="free"):
        self.name = name
        self.login = login
        self.password = password
        self.is_blocked = False
        self.subscription_date = subscription_date
        self.subscription_mode = subscription_mode

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if re.fullmatch(r"[А-Яа-яЁё]+", value):
            self._name = value
        else:
            raise ValueError("Имя должно содержать только буквы русского алфавита")

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        if re.fullmatch(r"[A-Za-z0-9_]{6,}", value):
            self._login = value
        else:
            raise ValueError("Логин должен содержать латинские буквы, цифры и подчёркивание, минимум 6 символов")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Пароль должен содержать не менее 6 символов")
        if not re.search(r"[a-z]", value):
            raise ValueError("Пароль должен содержать строчную букву")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Пароль должен содержать заглавную букву")
        if not re.search(r"[0-9]", value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        if not re.fullmatch(r"[A-Za-z0-9]+", value):
            raise ValueError("Пароль может содержать только латинские буквы и цифры")
        self._password = value

    def __str__(self):
        return f"{self.name} ({self.login}) — подписка: {self.subscription_mode}, действует до {self.subscription_date}"

try:
    user = User(
        name="Анна",
        login="Anna_01",
        password="Passw1",
        subscription_date=date(2025, 12, 31),
        subscription_mode="paid"
    )
    print(user)
except ValueError as e:
    print("Ошибка:", e)


