#coding=utf-8
__author__ = 'Bryan'

def make_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return  person

person1 = make_person('Bryan', 'bai', 38)
print(person1)
print(person1['age'])