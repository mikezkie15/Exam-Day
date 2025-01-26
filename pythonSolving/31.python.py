# Get a scale of 1 to 20 from the user
# Then display the salary according to employer scaLe

scale = int(input("Enter Number between 1 to 20: "))

if scale >= 20:
    print("Salary is 70,000")
elif scale >= 18:
    print("Salary is 50,000")
elif scale >= 15:
    print("Salary is 40,000")
elif scale >= 12:
    print("Salary is 20,000")
elif scale >= 9:
    print("Salary is 10,000")
else:
    print("Invalid ")