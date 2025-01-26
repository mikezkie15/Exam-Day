#get string input
#check if user input name of the week
#display holiday if user input Sunday

name_of_week = input("Enter name of the week: ")

if (name_of_week == 'Sunday' or name_of_week == 'sunday' or name_of_week == 'Sun' or name_of_week == 'sun'):
    print("Holiday")
elif (name_of_week == 'Saturday' or name_of_week == 'saturday' or name_of_week == 'Sat' or name_of_week == 'sat'):
    print("Sabbath Day")
else:
    print("Working Day")