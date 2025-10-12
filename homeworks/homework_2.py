class Person:
    def __init__(self, name, brith_date, occupation):
        self.name = name
        self.brith_date = brith_date
        self.occupation = occupation


    def introduce(self, data):
         print(f'Привет, меня зовут {self.name} я друг Азамжана, я родился {self.brith_date}, Работаю {self.occupation}')

class Friend(Person):
    def __init__(self, name, brith_date, occupation, hobby):
        super().__init__(name, brith_date, occupation)
        self.hobby = hobby

    def introduce(self, data):
         print(f'Привет, меня зовут {self.name} я друг Азамжана, я родился {self.brith_date}, работаю  {self.occupation}, в свободное время {self.hobby}')





class Classmate(Person):
    def __init__(self, name, brith_date, occupation, group_name):
        super().__init__(name, brith_date, occupation)
        self.group_name = group_name

    def introduce(self, data):
         print(f'Привет, меня зовут {self.name} я друг Азамжана, я родился в {self.brith_date}, учусь на {self.occupation}, в свободное время {self.group_name}')


classmate = Classmate("Артем", "октябре 23 числа 1990 года",  "", "читаю книги")
friend = Friend('Кирилл', "11 января 2000 года", "продавцом", hobby="играю в игры")
friend.introduce()
classmate.introduce()