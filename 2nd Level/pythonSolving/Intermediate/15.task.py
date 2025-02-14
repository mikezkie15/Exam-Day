import math

num = int(input("Enter a number: "))
next_num = num + 1
prev_num = num -1
print(f"This is your number input {num}")
print(f"This is the sin of the next number {math.sin(next_num)}")
print(f"This is the cos of the next number {math.cos(next_num)}")
print(f"This is the sin of the prev number {math.sin(prev_num)}")
print(f"This is the cos of the prev number {math.cos(prev_num)}")