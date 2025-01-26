# Get a Starting and Ending Number from the user
# with a decreasing step of 4

s = int(input("Enter a Starting Number: "))
e = int(input("Enter a Ending Number: "))

lst = []
for i in range(s,e+1):
    lst.append(i)

print(lst)