__author__ = 'Bryan'
#coding= utf-8

import json

numbers = [2, 3, 7, 5, 11, 13]
file_name = 'number.json'

with open(file_name, 'w') as file_obj:
    json.dump(numbers, file_obj)
