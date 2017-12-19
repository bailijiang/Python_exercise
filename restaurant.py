__author__ = 'Bryan'
#coding=utf-8

# 9-1 餐馆:创建一个名为 Restaurant 的类，其方法__init__()设置两个属性:
# restaurant_name 和 cuisine_type。创建一个名为 describe_restaurant()的方法和一个 名为 open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息， 指出餐馆正在营业。
# 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述 两个方法。

class Restaurant():
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0
    def describe_restaurant(self):
        print("Restaurant name is: " + self.restaurant_name.title())
        print("Restaurant cuisine type: " + self.cuisine_type)
    def open_restaurant(self):
        print(self.restaurant_name.title + "is openning.")
    def set_number_served(self, num):
        self.number_served = num
    def update_number_served(self, num):
        self.number_served += num

restaurant1 = Restaurant('翠满楼', '家常菜')
restaurant2 = Restaurant('顺峰', '海鲜')
restaurant3 = Restaurant('田老师', '快餐')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant4 = Restaurant('便宜坊', '烤鸭')
print(restaurant4.restaurant_name + " have served " + str(restaurant4.number_served) + " people.")
restaurant4.number_served = 188
print(restaurant4.restaurant_name + " have served " + str(restaurant4.number_served) + " people.")

restaurant4.set_number_served(288)
print(restaurant4.restaurant_name + " have served " + str(restaurant4.number_served) + " people.")
restaurant4.update_number_served(388)
print(restaurant4.restaurant_name + " have served " + str(restaurant4.number_served) + " people.")
