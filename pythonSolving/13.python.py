#Program to get password from user and check wether the password contain alphanumric character and length should be minimum of 8
#and maximum of 20
pwd = input("Enter your password: ")

if(len(pwd) >= 8 and len(pwd) <= 20):
    if(pwd.isalnum()):
        print("Your password is allowed: " + pwd)
    else:
        print("Your password contain white spaces and special chasracters: " + pwd)
else:
    print("Password length must be between 8 and 20 characters. Length: " + str(len(pwd))) 