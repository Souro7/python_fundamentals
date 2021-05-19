def sayHello(name='Tom'):
    """
    Print hello and then name.
    """
    print('Hello, ' + name)

sayHello()

def getSum(num1, num2):
    total = num1 + num2
    return total

# print(getSum(4, 5))

def addOneToNum(num):
    num =  num + 1
    return num

num = 5
print(addOneToNum(num))

# lambda function

getSum = lambda num1, num2 : num1 + num2

print(getSum(9, 2))