#Get 5 year from user
#Store in a array
#Display only the leap year# Get 5 years from the user and store them in a list
lst = []

for i in range(5):
    year = int(input(f"Enter year {i+1}: "))
    lst.append(year)

# Check and display if each year is a leap year or not
for year in lst:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap year")
    else:
        print(f"{year} is Not a Leap year")
