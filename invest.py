__author__ = 'Bryan'
#coding=utf-8


file_name = 'reason.txt'

with open(file_name, 'a') as file_obj:
    while True:
        reason = input("Why do you love programming? ")
        if reason == 'q':
            break
        file_obj.write(reason + "\n")
print("end...")