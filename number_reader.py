__author__ = 'Bryan'
#coding=utf-8

import json

filename = 'number.json'

with open(filename) as file_obj:
    numbers = json.load(file_obj)

print(numbers)