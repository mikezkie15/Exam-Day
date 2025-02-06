# Get a name from the list
# Display name that start with 'M'

names = ["Mike","Mark Ryan","Marky","Micheal","Mirasol","Lumber"]

for name in names:
    if name.startswith('M'):
        print(name)
    else:
        print("Dont start with the letter M " + name)