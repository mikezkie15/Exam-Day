# Display a list of student name in descending order
# And put A. at the end of every student name

student_names = ["Mike","Zyper kent","Rolith"]

student_names.sort(reverse=True)
for i in student_names:
    print(f"{i}.")