# Get a name from the user
# Check if it is in lowercase
# If not lowercase then convert into lowercase

name = input("Enter a name: ")

if name.islower():
    print("Name is already in a lowercase form " + name)
else:
    print("Name is converted into lower case " + name.lower())