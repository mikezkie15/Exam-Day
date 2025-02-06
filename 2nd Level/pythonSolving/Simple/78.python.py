# Get a number from the user
# return the next number with addition from user
# return the previous number with addition of user entered number

num_user = int(input("Enter a number: "))
num_user_next = int(input("Enter a number to add on the next: "))
num_user_previous = int(input("Enter a number to add on the previous: "))

num_user += 1
num_next = num_user + num_user_next
num_user -= 1
num_previous = num_user + num_user_previous

print("The number input by the user: " + str(num_user))
print("The next number added with " + str(num_user_next) + " is " + str(num_next))
print("The previous number added with " + str(num_user_previous) + " is " + str(num_previous))