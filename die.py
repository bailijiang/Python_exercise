__author__ = 'Bryan'
#coding=utf-8

from random import randint

class Die():
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        res = []
        for n in range(10):
            res.append(randint(1, self.sides))
        return res

die1 = Die()
print(die1.roll_die())
die2 = Die()
die2.sides = 10
print(die2.roll_die())