name = "Brad"
age = 37

# Concatenate
print('Hello, ' + name + ' and I am ' + str(age))

# String formatting

# arguments by position

print('{1}, {2}, {0}'.format('a', 'b', 'c'))

# arguments by name

print('My name is {name}'.format(name=name))

#fstrings (python 3.6+)

print(f'My name is {name}, and I am {age}')

# string methods

s = 'Hello there world'

print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())

print(len(s))

print(s.replace('world', 'everyone'))

sub = 'H'
print(s.count(sub))



