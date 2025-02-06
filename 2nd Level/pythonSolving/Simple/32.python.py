# Get two number from the user
# pass to function a find the minimum
# display the minimum number

first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
   
def find_min(a,b):
    if first > second:
        print(str(first) + " is greater than " + str(second) + " number")
    else:
        print(str(first) + " is less than " + str(second) + " number")

find_min(first,second)
