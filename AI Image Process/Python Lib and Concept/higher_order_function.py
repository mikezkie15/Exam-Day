def operation(func,a,b):
    return func(a,b)

def add(a,b):
    sum = a + b
    return sum

result = operation(add,2,3)

print(result)