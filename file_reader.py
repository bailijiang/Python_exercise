__author__ = 'Bryan'
#coding=utf-8

file_name = 'pi_digits.txt'

with open(file_name) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    for line in file_object:
        print(line.rstrip())

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))