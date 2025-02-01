# Make a list of number
# Display number divisible by 3 and 5

number_lst = [1,2,3,4,3,6,4,3,2,33,45,67,5,4343,]

for i in number_lst:
    if (i % 3 == 0) and (i % 5 == 0):
        print(i)