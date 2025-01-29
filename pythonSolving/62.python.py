# Get Different information of students from user
# Display all the student information
# After Displaying , Update User CNIC,Age,Contact


user_name = input("Enter your name: ")
father_name = input("Enter your father name: ")
user_cnic = input("Enter your CNIC: ")
user_age = input("Enter your Age: ")
user_contact = input("Enter your contact number")

def display_user_info (username,fathername,usercnic,userage,usercontact):
    print("Your name is " + str(username))
    print("Your Father name is " + str(fathername))
    print("Your CNIC is " + str(usercnic))
    print("Your Age is " + str(userage))
    print("Your Contact is " + str(usercontact))

display_user_info(user_name,father_name,user_cnic,user_age,user_contact)

print("Updated User Info")
user_cnic = input("Enter your CNIC: ")
user_age = input("Enter your Age: ")
user_contact = input("Enter your contact number")

print("Your CNIC is " + str(user_cnic))
print("Your Age is " + str(user_age))
print("Your Contact is " + str(user_contact))

