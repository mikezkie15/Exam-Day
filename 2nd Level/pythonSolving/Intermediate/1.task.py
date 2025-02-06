# Get a user input
# check the file extension
# if file extension is '.mp3' display a message "This File type is not allowed"


import os
user_input = input("Enter a file name: ")
file_name, file_extension = os.path.splitext(user_input)

if file_extension == ".mp3":
    print(f"This file type {file_name}{file_extension} is not Allowed !")
else:
    print(f"This file type {file_name}{file_extension} is allowed !")
    