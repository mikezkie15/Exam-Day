# Get 5 student name
# Check the first char of first student name
# is equal to the last student first char

lst = []

for i in range(2):
    lst.append(input("Enter a Student Name: "))

std_1 = lst[0]
std_2 = lst[-1]

if std_1[0].lower() == std_2[0].lower():
    print(f"The first char of the student name is equal")
else:
    print(f"The first char of the student name is not equal")