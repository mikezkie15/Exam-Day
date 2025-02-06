# Get a Large Number and Lower Number
# Display large to Lower
# And find their sum.

large = int(input("Enter a large number: "))
small = int(input("Enter a small number: "))

s = 0
for i in range(large,small,-1):
    print(i)
    s += i
print(s)
