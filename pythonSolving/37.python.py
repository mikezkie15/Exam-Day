# Get six number from the user
# Square the first three number
# Cube the next three number

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
num3 = int(input("Enter a number:"))
num4 = int(input("Enter a number:"))
num5 = int(input("Enter a number:"))
num6 = int(input("Enter a number:"))

def cube_num (a):
    return a ** 3

def square_num (a):
    return a ** 2

print(square_num(num1))
print(square_num(num2))
print(square_num(num3))

print(cube_num(num4))
print(cube_num(num5))
print(cube_num(num6))