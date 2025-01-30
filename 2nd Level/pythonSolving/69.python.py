# Create file
# get name and age
# write on the file

name = input("Enter your name: ")
age = input("Enter your age: ")

file = open("Mike.txt","w+")
file.write("Your name is " + str(name) + " and " + str(age))
file.close()


