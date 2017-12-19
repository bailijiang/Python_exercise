__author__ = 'Bryan'
#coding=utf-8

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return  long_name.title()
    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back odometer.")
    def increment_odometer(self, miles):
        self.odometer += miles

my_new_car = Car('bmw', '330i', '2017')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer = 23
my_new_car.read_odometer()
my_new_car.update_odometer(33)
my_new_car.read_odometer()
my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'brz', 2013)
my_used_car.update_odometer(23550)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()