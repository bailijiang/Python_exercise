__author__ = 'Bryan'

squares = []
for num in range(1,11):
    square = num ** 2
    squares.append(square)

print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)