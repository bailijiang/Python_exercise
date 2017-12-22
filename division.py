__author__ = 'Bryan'
#coding=utf-8


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)