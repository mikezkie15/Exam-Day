# Get 2 Number from user
# Find their cube
# Add both result and display to user

num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))

def cube_add (a,b):
    print("Cube of num1 is " + str(a ** 3))
    print("Cube of num2 is " + str(b ** 3))
    print("Total is : " + str((a **3)+(b **3)))

cube_add(num1,num2)

