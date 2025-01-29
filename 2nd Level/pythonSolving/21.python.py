#get five number from user
#store in s array
#find and display the minum 

import array as arr

a = arr.array('i',[])
for i in range(5):
    a.append(int(input("Enter the " + str(1+i) + " number: ")))
minn = a[0]

for j in range(5):
    print(a[j])
    if(a[j] < minn):
        minn = a[j]
print(minn)
