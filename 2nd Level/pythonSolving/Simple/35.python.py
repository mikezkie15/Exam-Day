# Get 10 student name from the user
# Store in a list
# Display the list
# Display the student name in reverse order
# Also remove the last and first element of the list

lst = []
for i in range(1,11,1):
    lst.append(input( str(i) + ". Enter a Name: "))

print(lst)

lst.sort(reverse=True)
del lst[0]
lst.pop()

print("Deleted first and last element of the list and reverse")
print("The list the updated list " + str(lst))