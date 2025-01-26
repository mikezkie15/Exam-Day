# Get a Binary from the user
# Convert Binary to Decimal using a function
# Display the converted Decimal
from unicodedata import decimal

binary = (input("Enter a Binary sequence: "))

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

print(f"The Binary : {binary} is Converted into Decimal {binary_to_decimal(binary)}")