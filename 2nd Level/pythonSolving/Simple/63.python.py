# Get a list of number from the user
# Store in a list
# Using a function find the minimum 

lst = []

for i in range(4):
    lst.append(input(f"Enter a {i+1} number:"))

def find_min(l):
    print(min(lst))

find_min(lst)  