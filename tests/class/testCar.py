class Freshener:
    def __init__(self):
        self.message = 'i freshener'
    def info(self):
        return self.message


class Car:
    static_field = 'me static_field in class Car'
    def __init__(self,):
        self.fheshener = Freshener()


car = Car()
print(car)
print(car.fheshener.info())
print(Car.static_field)
print(car.static_field)
Car.static_field = 'i rewrite'
print(Car.static_field)
print(car.static_field)

