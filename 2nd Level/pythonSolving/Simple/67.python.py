# Get two number from user
# Find the sum of two number
# 1st number should be positive
# 2nd number should be negative
# Less than 50
# Greater 20

num1 = int(input("Enter your 1st number: "))
num2 = int(input("Enter your 2nd number: "))

if ((num1 >0 ) and (num2 <0 and num2 > -20 )):
    print(num1 + num2)
else:
    print("Invalid")