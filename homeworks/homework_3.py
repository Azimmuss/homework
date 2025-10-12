class Person:
    def __init__(self, name, brith_day, occupation, higter_education):
        self.name = name
        self.brith_day = brith_day
        self.__occupation = occupation
        self.__higter_education = higter_education

    def introduce(self, data):
         print(f'Привет, меня зовут {self.name} я друг Азамжана, я родился {self.brith_day}, Работаю {self.__occupation} высшего оброзования {self.__higter_education}')



class Friend(Person):
    def __init__(self, name, brith_day, occupation,  higter_education, hobby):
        super().__init__(name, brith_day, occupation, higter_education)
        self.hobby = hobby

    def introduce(self, hobby):
         print(f'Привет, меня зовут {self.name} я друг Азамжана, я родился {self.brith_day}, работаю  {self._Person__occupation}, высшего оброзования {self._Person__higter_education}, в свободное время {self.hobby}')





class Classmate(Person):
    def __init__(self, name, brith_day, occupation,  higter_education, group_name):
        super().__init__(name, brith_day, occupation,  higter_education)
        self.group_name = group_name

    def introduce(self, group_name):
         print(f'Привет, меня зовут {self.name} я однаклассник Азамжана, я родился в {self.brith_day}, учусь на {self._Person__occupation}, высшего оброзования {self._Person__higter_education}, мы в {self.group_name} группе')




classmate = Classmate("Артем", "октябре 23 числа 1990 года",  "доктора", "нету", 5)
friend = Friend('Кирилл', "11 января 2000 года", "продавцом", "нет", "играю в игры")
friend.introduce(5)
classmate.introduce("играю в игры")
