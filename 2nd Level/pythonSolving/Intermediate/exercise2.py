name = input("Enter your name: ")
num_sub = int(input("Enter the number of subject: "))
lst = []
for i in range(num_sub):
    grade = float(input(f"Enter your grade {i+1}:"))
    lst.append(grade)
total_avg = sum(lst) / num_sub
print(name," total average is ",total_avg)

if 90 <= total_avg <= 100:
    print(name," is Excellent")
elif 80 <= total_avg <= 90:
    print(name," is Very Good")
elif 75 <= total_avg <= 80:
    print(name," is Good")
else:
    print(name," is Failed")
