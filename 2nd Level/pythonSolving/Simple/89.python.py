# Get a number from 0 to 10 only divisible by 3
# Get a number from 0 to 10 only divisible by 5
# Add both generated number to each other to display total result
divisibleBy3 = 0
divisibleBy5 = 0

for i in range(20):
    if i % 3 == 0:
        divisibleBy3 += i
print(divisibleBy3)

for i in range(20):
    if i % 5 == 0:
        divisibleBy5 += i
print(divisibleBy5)
print(f"The total of both number is {divisibleBy3 + divisibleBy5}")