# Get 10 number from the user
# Store in list
# Find the Products and Sum
# Add both and then Display to user

lst = []

for i in range(10):
    lst.append(int(input("Enter a number: ")))


another_sum = sum(lst)
product = 1
for i in lst:
    product *= i

total = another_sum + product
print(another_sum)
print(f"The sum of the list is {another_sum}")
print(f"The product of the list is {product}")
print(f"The total sum and product of the list is {total}")