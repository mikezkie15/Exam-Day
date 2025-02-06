# Get a number from the user
# store in a list
# add only even number

num_lst = []
user_input = int(input("Enter a number: "))

if user_input %2 == 0:
    print("Number even number is added to the  list")
    num_lst.append(user_input)
else:
    print("Number is not added give only odd number")