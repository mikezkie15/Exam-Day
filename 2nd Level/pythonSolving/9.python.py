#Get two number from user and display two table
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def table(num1,num2):
    for i in range(1,11):
        print( str(i) + " * " + str(num1) + "  = " + str(i*num1) +
        "\t\t" + str(i) + " * " + str(num2) + "  = " + str(i*num2))

table(num1,num2)