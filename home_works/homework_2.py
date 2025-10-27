class Person:
    def __init__(self, name, brith_day, occupation):
        self.name = name
        self.brith_day = brith_day
        self.occupation = occupation

    def introduce(self, data):
         print(f'Привет, меня зовут {self.name} я друг Азамжана, я родился {self.brith_day}, Работаю {self.occupation}')



class Friend(Person):
    def __init__(self, name, brith_day, occupation, hobby):
        super().__init__(name, brith_day, occupation)
        self.hobby = hobby

    def introduce(self, hobby):
         print(f'Привет, меня зовут {self.name} я друг Азамжана, я родился {self.brith_day}, работаю  {self.occupation}, в свободное время {self.hobby}')





class Classmate(Person):
    def __init__(self, name, brith_day, occupation, group_name):
        super().__init__(name, brith_day, occupation)
        self.group_name = group_name

    def introduce(self, group_name):
         print(f'Привет, меня зовут {self.name} я однаклассник Азамжана, я родился в {self.brith_day}, учусь на {self.occupation},  мы в {self.group_name} группе')




classmate = Classmate("Артем", "октябре 23 числа 2007 года",  "доктора", 5)
friend = Friend('Кирилл', "11 января 2008 года", "продавцом", "играю в игры")
friend.introduce(5)
classmate.introduce("играю в игры")
