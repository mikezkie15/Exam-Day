#Get a user char
#Check wether its vowel or consonant 
#also if it is a number
char = input("Enter a char or a number: ")

if(char == 'a' or char =='A'):
    print("Its a vowel")
elif(char == 'i' or char =='I'):
    print("Its a vowel")
elif(char == 'e' or char =='E'):
    print("Its a vowel")
elif(char == 'u' or char =='U'):
    print("Its a vowel")
elif(char == 'o' or char =='O'):
    print("Its a vowel")
elif(char.isdigit()):
    print("Its a number")
else:
    print("Its a consonant")