# DICTIONARY -> unordered, changable, indexed. No duplicates


person = {
    'first_name': 'John',
    'last_name': 'Wick',
    'age': 30
}

print(person['first_name'])
print(person.get('last_name'))

person['phone'] = '555-555-5555'

print(person['phone'])

print(person.keys())
print(person.items())

# make copy

person2 = person.copy()

person2['city'] = 'Boston'

# remove item

del(person['age'])
person.pop('phone')

# clear
person.clear()

print(person)

# list of dictionaries

people = [
    {'name': 'martha', 'age': 40},
    {'name': 'nick', 'age': 25}
]

print(people)