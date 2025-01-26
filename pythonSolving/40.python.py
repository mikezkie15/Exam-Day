# Get username from user
# Check the username should contain alphanumeric char
# And username length should not be less than equal to 8

user = input("Enter a username: ")

def check_user(u):
    if len(u) >= 8 :
        if u.isalnum():
            print("The username " + u + " is valid.")
        else:
            print("The username contain special characters and white spaces  ")
    else:
        print("the username is less than 8 characters")


check_user(user)