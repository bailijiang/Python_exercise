__author__ = 'Bryan'

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods: ")
print(my_foods)


print("\nMy friend foods:")
print(friend_foods)

my_foods.append('calooni')
friend_foods.append('ice cream')

print("My favorite foods: ")
print(my_foods)


print("\nMy friend foods:")
print(friend_foods)


test1 = "Three items from the middle of the list are:"
print(test1[int(len(test1)/2-1):int(len(test1)/2+2)])

for food in my_foods:
    print(food.title())