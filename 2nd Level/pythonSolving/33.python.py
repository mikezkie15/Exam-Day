# Get element from the user
# Store it in a list
# Count the element of the list
# Print the element of the list

lst = []

for i in range(5):
    element = input("Enter " + str(i) + " : " )
    lst.append(element)

print("The list contain " + str(len(lst)) + "element")

for l in lst:
    print(l)
