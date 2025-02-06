# Get a sentence from the user
# reverse sentence
# and enclose in double Quotation and put a full stop at the end of the sentence

sentence = input("Enter a sentence:")

reverse_sentence = sentence[::-1]

print(f'"{reverse_sentence}."')