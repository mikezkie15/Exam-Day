# Get a sentence from the user
# find the occurrence of a specific word or char
# then replace with another word

sentence = input("Enter a sentence: ")
find = input("Enter target word or char: ")
change = input("Enter to change into:")
times = sentence.count(find)
change_into = sentence.replace(find,change)

print(f"Your sentence is '{sentence}' and target word is '{find}'")
print(f"The target word occur {times} in your sentence")
print(f"Your updated sentence is {change_into}")