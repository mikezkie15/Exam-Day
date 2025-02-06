# Get a Name of different Student from user
# store in a list
# store only if the student is start from char a and end at char a

names = []

for i in range(2):
    name = input("Enter a student name: ")
    if name.startswith("D") and name.endswith("e"):
        names.append(name)
print(names)
