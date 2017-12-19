#coding=utf-8
__author__ = 'Bryan'

def greet_user(username):
    """显示简单的问候语"""
    print("Hello " + username.title() + "!")

# greet_user("Bryan")

def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return  full_name.title()

while True:
    print("\nYou can enter your name.")
    print("Enter 'q' any time to quit program.")

    f_name = input('first name: ')
    if f_name == 'q':
        break
    l_name = input('last_name:')
    if l_name == 'q':
        break
    full_name = get_formatted_name(f_name, l_name)

    print("\nHello, " + full_name + " you are welcome!")