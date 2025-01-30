# Get 6 ID number from user
# display list
# clear the list
#
lst = []

for i in range(6):
   lst.append(int(input("Enter a unique ID: ")))

print(lst)

lst.clear()

if len(lst) == 0:
    print(f"The is empty {len(lst)}")
else:
    print(f"The list has {len(lst)} element")

