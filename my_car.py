__author__ = 'Bryan'
#coding=utf-8

from car import Car, ElectricCar, Battery

my_new_car = Car('bmw', '330i', '2017')
print(my_new_car.get_descriptive_name())

my_new_car.odometer = 23
my_new_car.read_odometer()

