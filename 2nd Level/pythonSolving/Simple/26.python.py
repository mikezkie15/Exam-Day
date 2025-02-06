#Get a Number
#Check whether is it odd or even
#And then find that Number squeare

number = int(input("Enter a Number: "))
if (number%2 == 0):
    print("Number is Even")
    print("The square of " + str(number)+ " is "+  str(number ** 2))
else:
    print("NUmber is Odd")