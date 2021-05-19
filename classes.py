# CLASS - blueprint for creating objects. 
# An object has properties and methods associated with it. 
# Almost everything in python is an object

# create class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'Hello, my name is {self.name} and I am {self.age}'

    def hasBirthday(self):
        self.age += 1

# extending a class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance
    
    def greeting(self):
        return f'Hello, my name is {self.name} and I owe {self.balance}'




# init user object

brad = User('Brad', 'brad@email.com', 23)
janet = User('Janet', 'janet@email.com', 23)

print(brad.name)
print(janet.email)

greeting = brad.greeting()

print(greeting)

brad.hasBirthday()

print(brad.greeting())


# init customer

john = Customer('John', 'john@email.com', 35)

john.setBalance(5000)

print(john.greeting())