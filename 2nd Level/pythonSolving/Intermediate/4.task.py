# Get a password from user that should contain alphanumeric,special character
# and the length should be more than 8 and less than 20 char
# Restrict user from including Uppercase and space
import re
password = input("Enter a password: ")

if len(password) > 8 and len(password) < 20:
    print("Password must be more than 8 and less than 20 characters.")
if any(char.isupper() for char in password):
    print("Password should not contain uppercase letters.")
if " " in password:
    print("Password should not contain spaces.")
    if not re.search(r"\d", password) or not re.search(r"[a-z]", password):
        print("Password must contain at least one digit and one lowercase letter."
)
else:
    print("password is okay")