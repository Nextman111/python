class Persone:
    _this_is = 'Persone'

    def __init__(self, name='Unknown', last_name='Unknown', age=0):
        self.__name = name
        self.__last_name = last_name
        self.__age = age

    def info(self):
        return f'{self._this_is} - name: {self.__name}, last_name: {self.__last_name}, age: {self.__age}'


class Employer(Persone):
    _this_is = 'Employer'

    def __init__(self, name, last_name, age, inn, number, snils):
        super().__init__(name, last_name, age)
        self.__inn = inn
        self.__number = number
        self.__snils = snils

    def info(self):
        return f'{super().info()}, inn: {self.__inn}, number: {self.__number}, snils: {self.__snils}'


vasiliy = Persone(name='Vasiliy', last_name='Pupkin', age=55)
print(vasiliy.info())

viktor = Employer(name='Victor', last_name='Petrov', age=22, inn=9929, number=3, snils=133321123)
print(viktor.info())

