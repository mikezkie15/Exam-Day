# Get 2 number from the user
# swap their value without creating a temp variable

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("Before the swap")
print("a is = " + str(a))
print("b is = " + str(b))
a, b = b, a
print("After the swap")
print("a is = " + str(a))
print("b is = " + str(b))

