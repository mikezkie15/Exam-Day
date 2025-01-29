a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter an operation: ")

def arithmetic_operation(a,b,op):
    if(op == '+'):
        print("The sumation is: " + str(a+b))
    elif(op == '-'):
        print("The subtarction is: " + str(a-b))
    elif(op == '/'):
        print("The coefficient is: " + str(a/b))
    elif(op == '*'):
        print("The multiplication is: " + str(a*b))

arithmetic_operation(a,b,op)
