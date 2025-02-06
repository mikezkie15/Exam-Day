# Get 10 float data type from the user
# convert to int
# display to the user

lst = []
converted_int = []
for i in range(10):
    lst.append(float(input("Enter a floating point number: ")))
print("The element inside the list " + str(lst))
for k in lst:
    if type(k) == float:
        converted_int.append(int(k))
print("This is the converted data type: " + str(converted_int))