# Read existing file
# Get two number from user and add result and
# Display existing file

file = open("Mike.txt","r+")

print(file.read())

num1 = int(input("Enter a number: "))
num = int(input("Enter a number: "))
file.write("First num is " + str(num1) + " Second number is " + str(num))
file.close()