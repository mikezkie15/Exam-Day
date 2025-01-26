#Get three number from user and display the maximum number.
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if (num1 > num2):
    print("1st Number is the Maximum " + str(num1))
elif(num3 > num2):
    print("3rd Number is the Maximum " + str(num1))
else:
    print("2nd Number is the Maximum " + str(num1))
