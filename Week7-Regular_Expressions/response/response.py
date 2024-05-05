from validator_collection import validators

s = input("What's your email address? ").lower().strip()

try:
    validators.email(s)
    print("Valid")
except:
    print("Invalid")
