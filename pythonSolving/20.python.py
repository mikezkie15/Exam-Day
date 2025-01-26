#get five number from user
#store in s array
#find and display the maximum 

import array as arr

a = arr.array('i',[])
for i in range(5):
    a.append(int(input("Enter the " + str(1+i) + " number: ")))


print(a)
print(str(max(a)))