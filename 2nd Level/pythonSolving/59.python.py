# Get a Bio from a user
# Ge a target word
# Count Specific word

user_bio = input("Enter a bio: ")
target_word = input("Enter target word: ")

count_occr = user_bio.split().count(target_word)

print(f"The bio {user_bio}  target word occur {count_occr}")