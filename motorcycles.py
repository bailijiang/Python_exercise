__author__ = 'Bryan'

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'BRZ')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

poped_motocycles = motorcycles.pop()
print(poped_motocycles)

first_owned = motorcycles.pop(0)
print(first_owned.title())

motorcycles.remove('suzuki')
print(motorcycles)