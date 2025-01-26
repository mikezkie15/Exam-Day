# Find the area of triangle
# get a number from the user
# find the square of that number
# add the square with area of the triangle

def area_triangle(base,height):
    area = 0.5 * base * height
    return area
a = int(input("Enter a base: "))
b = int(input("Enter a height: "))

num =  int(input("Enter a number : "))
squared = num ** 2
trai = area_triangle(a,b)
print("The area of triangle is " + str(trai))
print("Total with add square : " + str(squared + trai))

