name = input("Enter your name: ")
num_sub = int(input("Enter the number of subject: "))
total_grade = 0
for i in range(num_sub):
    grade = int(input(f"Enter grade {i+1}: "))
    total_grade += grade

total_avg = total_grade / num_sub
print(name," total average is ",total_avg)

if total_avg >= 90:
    print(name," Grade is Excellent")
elif total_avg >= 80:
    print(name," Grade is Very Good")
elif total_avg >= 75:
    print(name," Grade is Good")
else:
    print(name," Grade is Failed")


