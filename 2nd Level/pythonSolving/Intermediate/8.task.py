# Get the length of the password
# Generate the passsword
# Display the generated password

import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 for security."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# User input
length = int(input("Enter the desired password length: "))
print("Generated Strong Password:", generate_password(length))
