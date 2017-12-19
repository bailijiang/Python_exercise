__author__ = 'Bryan'
#coding=utf-8

from car import Car

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_electric_car = ElectricCar('tesla', 'model s', 2017)
print(my_electric_car.get_descriptive_name())