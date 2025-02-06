# Get a sentence from the user
# Remove any char from a string

sentence = input("Enter a sentence: ")
print(sentence)
needRemoved =  input("Enter a char to remove: ")
removed_s = sentence.replace(needRemoved,"")
print(removed_s)