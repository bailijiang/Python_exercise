#coding=utf-8
__author__ = 'Bryan'


def greet_users(names):
    for name in names:
        msg = "Hello" + " " + name.title()
        print(msg)

names = ['bryan', 'heero', 'bailijiang']
greet_users(names)