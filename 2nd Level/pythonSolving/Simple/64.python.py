# Program to find the Scholarship 
# for student in admission
# On the basis of student Marks
# Using a function

marks = int(input("Enter Students Marks: "))

def check_marks(marks):
    if marks >= 11000:
        print("Free Education")
    elif marks > 1000:
        print("80% Monthly Fess Deduction")
    elif marks > 900:
        print("60% Monthly Fess Deduction")
    elif marks > 800:
        print("40% Monthly Fess Deduction")
    elif marks > 700:
        print("30% Monthly Fess Deduction")
    else:
        print("There is No Scholarship")

check_marks(marks)