#Get a Number
#Check wether the number is negative or postive and equal to zero

num = int(input("Enter a Number: "))

if (num > 0):
    print("The " + str(num) + " is a Positive Number")

elif(num == 0):
    print("The " + str(num) + " 0is Equal to " + str(num))
else:
    print("The number is a Negative Number")