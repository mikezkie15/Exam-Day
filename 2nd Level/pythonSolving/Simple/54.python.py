# Get a number for the user
# use for loop to find the factorial of a number

number = int(input("Enter a number: "))
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(f"The factorial of {number} is {factorial(number)}")