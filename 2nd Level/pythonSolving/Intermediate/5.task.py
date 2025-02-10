# Get a 3 Student Name add in a list and display 
# Update any student on run time

lst = []
for i in range(3):
    s = input("Enter a student name: ")
    lst.append(s)
for i, name in enumerate(lst,1):
    print(f"{i} {name}")
index_update = int(input("Enter index to update: "))
update_name = input("Enter your update name: ")
lst[index_update-1] = update_name
for i, name in enumerate(lst, 1):
    print(f"{i} {name}")
