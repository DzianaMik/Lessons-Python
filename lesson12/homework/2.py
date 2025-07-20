"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title (len<50), year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
    def __init__(self, author: str, title: str, year: int):
        self.author = author     
        self.title = title     
        self.year = year
    
    @property
    def author(self):
        return self.__author
    
    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("No")
        if value <= 0 or value > CURRENT_YEAR:
            raise ValueError(f"{CURRENT_YEAR}.")
        self.__year = value

    def __lt__(self, other):  
        return self.year < other.year

    def __eq__(self, other):  
        return self.year == other.year

    def __gt__(self, other):  
        return self.year > other.year