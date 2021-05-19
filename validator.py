import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", email))