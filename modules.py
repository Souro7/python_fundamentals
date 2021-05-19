# A module is a file containing a set of functions to include in your application

# core modules
#------------------

# import datetime

from datetime import date

print(date.today())

from time import time

print(time())

# using pip modules
#------------

# pip3 install camelcase
# pip3 freeze -> shows installed modules

import camelcase

camel = camelcase.CamelCase()

text = 'hello there world'

print(camel.hump(text))


# custom modules
#----------------

import validator

print(validator.validate_email("abcd@gmail.com"))



