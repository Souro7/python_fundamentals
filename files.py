# Open / create a file

myFile = open('myFile.txt', 'w')

# get some info

print('Name: ', myFile.name)

print(f'Is closed: {myFile.closed}')

print(f'Opening mode: {myFile.mode}')


# w rite to file

myFile.write('I love python!')
myFile.write(' I also love JS!')
myFile.close()

# append to file

myFile = open('myFile.txt', 'a')
myFile.write(' I also like PHP')
myFile.close()

# read from file

myFile = open('myFile.txt', 'r+')

text = myFile.read(10)

print(text)


