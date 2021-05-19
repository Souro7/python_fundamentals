import json

sampleJSON = '{"first_name": "John", "last_name": "Doe"}'

# json to dict
user = json.loads(sampleJSON)

print(user)

# dict to json

car = {'make': 'Ford', 'model': 'Mustang'}

carJSON = json.dumps(car)

print(carJSON)

