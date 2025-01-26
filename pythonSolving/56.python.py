# Get a decimal from the user
# convert Decimal to Binary
# Then display the converted decimal

dec = int(input("Enter a Decimal number: "))

converted_decimal = bin(dec).replace("0b","")

print(converted_decimal)