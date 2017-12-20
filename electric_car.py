__author__ = 'Bryan'
#coding=utf-8

from car import Car

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + " -kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif range == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    # def describe_battery(self):
    #     print("This car has a " + str(self.battery_size) + " -kWh battery.")

# my_electric_car = ElectricCar('tesla', 'model s', 2017)
# print(my_electric_car.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model x', 2017)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()