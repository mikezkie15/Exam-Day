# Get 5 Student Marks
# Store in a array
# Get Student Name
# Find and display the total Average
# Display each subject marks

import array as arr

a = arr.array('i',[])

student = input("Enter Student Name: ")
print("Enter marks in this order English, AI, Physics, Computer, Math")
for i in range(5):
    a.append(int(input("Enter your marks: ")))

total = 0
for j in range(len(a)):
    total += a[j]

print("Hi " + student  )
print("Your total Average marks is " + str(total/len(a)))

print("See your all subject marks")
print("English = " + str(a[0]))
print("AI = " + str(a[1]))
print("Physics = " + str(a[2]))
print("Computer = " + str(a[3]))
print("Math = " + str(a[4]))
