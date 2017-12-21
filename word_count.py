__author__ = 'Bryan'
#coding=utf-8


def count_words(filename):
    try:
        with open(filename) as file_obj:
            contents = file_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exsit."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")


filename = 'alice.txt'

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)