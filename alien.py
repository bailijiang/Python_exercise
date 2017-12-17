__author__ = 'Bryan'

# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])
#
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points")

# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
#
# alien_0['color'] = 'yellow'
# print(alien_0['color'])

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
#
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# alien_0['x_position'] += x_increment
# print("New x_position: " + str(alien_0['x_position']))
#
# print(alien_0)
# del alien_0['speed']
# print((alien_0))

aliens = []
for alien in range(30):
    aliens.append({'color': 'green', 'points': 5, 'speed': 'slow'})
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens:
    print(alien)