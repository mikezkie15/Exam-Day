# get  userinput
# add into a list only if the string is at a lowercase

lst_word = []
user_input = input("Enter a word: ")
if user_input.islower():
    lst_word.append(user_input)
else:
    print("Error enter a lower case word")
print(lst_word)