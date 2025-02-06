# Get a sentence from the user
# Should display all the characters except the last 10 char

user_input = input("Enter a sentence: ")
minus_las10 = user_input[:-10]
print(f"Your sentence is {user_input}")
print(f"Minus the last 10 char {minus_las10}")
