# Get length from user
# Find the area an parameter of a square
# Also find the square root of area and parameter

import math
l = float(input("Enter a length: "))


def square_of_area_parameter(l):
    area = l * l
    parameter = 4 * l
    area_square = math.sqrt(area)
    parameter_square = math.sqrt(parameter)

    print(f"The squared area is " + str(area_square))
    print(f"The squared paramater is " + str(parameter_square))

square_of_area_parameter(l)
s