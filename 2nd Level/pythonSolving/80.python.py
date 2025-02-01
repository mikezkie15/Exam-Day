# Get a string from the user
# Print char from the string that are present at an even index number\

user_string = input("Enter a sentence: ")
string_len = len(user_string)

for i in range(1,string_len):
    if i%2==0:
        print(user_string[i])
    else:
        print(i)

