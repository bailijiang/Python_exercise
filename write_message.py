__author__ = 'Bryan'
#coding=utf-8

file_name = 'programming.txt'

with open(file_name, 'a') as file_obj:
    file_obj.write("I also love finding meaning in large datasets.\n")
    file_obj.write("I love creating apps that running in a browser.\n")