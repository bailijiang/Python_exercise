__author__ = 'Bryan'
#coding= utf-8

file_name = 'note.txt'

with open(file_name) as file_obj:
    lines = file_obj.readlines()

replace_text = ''
for line in lines:
    replace_text += line.replace('Python', 'C/C++')

print(replace_text)