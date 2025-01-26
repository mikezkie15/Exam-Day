add = lambda x,y: x + y
#print(add(100,50))

cube = lambda x: x * x * x
#print(cube(5))

def operation(func,a):
    return func(a)

print(operation(cube,5))

#lambda function serves as an function-
#arguments for other function