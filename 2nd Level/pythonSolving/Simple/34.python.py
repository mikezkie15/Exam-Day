# Get 5 color from the user
# Store in a list
# Display the list
# Remove the first color
# Then display the color updated list

lst = []

for i in range(5):
    lst.append(input("Enter a color: "))

print("This are the element of the list " + str(lst))

del lst[0]

print("This are the updated element of the list " + str(lst))

