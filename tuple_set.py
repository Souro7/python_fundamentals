# Tuples: ordered, unchangeable, allows duplicate

fruit_tuple = ('Apple', 'Orange', 'Mango')

# get single value

# print(fruit_tuple[1])

# fruit_tuple[1] = 'Grape'  --> unchangeable

# tuples with one value should have trailing comma

fruit_tuple2 = ('Apple',)

del fruit_tuple2

# print(fruit_tuple2)

#---------------------------------------------------------------
# Set: unordered and unindexed, no duplicates

fruit_set = {'Apple', 'Orange', 'Mango', 'Apple'}

print(fruit_set)

print('Apple' in fruit_set)

fruit_set.add('Grape')
fruit_set.remove('Mango')

fruit_set.clear()

del fruit_set

print(fruit_set)