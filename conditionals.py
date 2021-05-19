x = 6
y = 5

# if x == y:
    # print(f'{x} is equal to {y}')

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{x} is less than {y}')

# membership operators -  in, not in

numbers = [1, 2, 3, 4, 5]

if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x in numbers)

# identity operators - is, is not

if x is y:
    print(x is y)

if x is not y:
    print(x is y)