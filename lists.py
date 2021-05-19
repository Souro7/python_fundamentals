# LIST: collection which is ordered and changable

numbers = [1, 2, 3, 4, 5]

letters = list(('a', 'b', 'c'))

print(type(numbers))

print(letters)

#------------

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(fruits[1])

print(len(fruits))

fruits.append('Mangoes')

fruits.remove('Grapes')

fruits.insert(2, 'Strawberries')

fruits.pop(3)

fruits.reverse()

fruits.sort(reverse=True)

print(fruits)

