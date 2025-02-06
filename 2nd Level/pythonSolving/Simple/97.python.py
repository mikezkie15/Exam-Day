# Create a list of integer
# find the middle element and its square root
# Display it

import math

lst_int = [1,2,5,6,7,5,3,2]
middle = len(lst_int)/2
square_root = math.sqrt(lst_int[int(middle)])

print("The list is ",lst_int)
print("The middle of the list ",middle)
print("The square root ",square_root)
