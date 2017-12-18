#coding=utf-8
__author__ = 'Bryan'

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet('hamster', 'harry')
describe_pet('dog', 'wille')

describe_pet(pet_name='billy', animal_type='cat')
describe_pet(pet_name='dahuang')