# Get user student marks and name
# Display Student marks and student name

std_dic = {}

for i in range(2):
    std_name = input("Enter a student name: ")
    std_marks = input("Enter a student marks: ")
    std_dic[std_name] = std_marks

print(dict)

std_list = list(std_dic.items())
if len(std_list) > 1:
    second_student = std_list[1]
    print(second_student)
    print(f"The second person is {second_student[0]} and his marks are {second_student[1]}")
else:
    print("Only one student was entered.")