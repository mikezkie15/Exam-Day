# Get Number from user
# Check whether the input is divisible by 5 and 6

num = int(input("Enter a Number: "))

if (num % 5 == 0 and num % 6 == 0):
    print(str(num) + " is Divisible By 5 and 6")
elif (num % 5 == 0):
    print(str(num) + " is Divisible By 5")
elif (num % 6 == 0):
    print(str(num) + " is Divisible By 6")
else:
    print(str(num) + " is Not Divisible by 5 or 6")
