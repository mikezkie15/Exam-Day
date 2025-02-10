# get a radius from the user
# calculate the circumference and area
# half the answer of both circumference and area
# display to the user

import math

radius = float(input("Enter a radius: "))

circumference = 2*math.pi*radius
print(f"The circumference is {circumference}")
area = 2*math.pi**2
print(f"The area is {area}")

add_half = (circumference/2) + (area/2)
print(f"Added the half of both number {add_half}")