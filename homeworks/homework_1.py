from bisect import bisect_right


class Person:
    def __init__(self, name, brith_date, occupation, higter_education):
        self.name = name
        self.brint_date = brith_date
        self.occupation = occupation
        self.higter_education = higter_education

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Дата рождения: {self.brint_date}")
        print(f"Профессия: {self.occupation}")
        print(f'Высшее образования: {self.higter_education}')

person_1 = Person("Андрей","22.12.1999", "Строитель", "Нет")

person_2 = Person("Мадина","03.16.2007", "Блогер", "Нет")

person_3 = Person("Макс","19.02.1990", "Архитектор", "Да")



person_1.info()
person_2.info()
person_3.info()
