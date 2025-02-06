# Get A Angle from the user
# Find its sin and cos
# Convert their result into degree unit
import math
from math import radians

angle = float(input("Enter a Angle: "))
sin_value = math.sin(angle)
cos_value = math.cos(angle)

sin_deg = radians(sin_value)
cos_deg = radians(cos_value)

print("The sin value of " + str(angle) + " in degree is " + str(sin_deg))
print("The cos value of " + str(angle) + " in degree is " + str(cos_deg))
