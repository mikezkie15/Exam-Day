#Get Student Name
#Check Student is "xyz"
#Then Don't Allow Him to take admission

student_name = input("Enter Student Name: ")

if student_name.lower() == "xyz":
    print("Your are not allowed " + student_name )
else:
    print("You are allowed " + student_name)