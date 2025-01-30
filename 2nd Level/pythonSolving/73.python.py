# Get a Sentence from the user
# Count the specific word in sentence


sentence = input("Enter a sentence: ")
target_word = input("Enter your target word or char:")
count = sentence.count(target_word)

print(f"This is your sentence: {sentence}")
print(f"Your target word occur {count} times")
