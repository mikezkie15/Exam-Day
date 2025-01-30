# Get user input of different color code
# Display in asc and dsc order of list

lst_color = []

for i in range(5):
    lst_color.append(input("Enter a color code to stor: "))

lst_color.sort()
print(f"Sort in a Ascending Order '{lst_color}'")

lst_color.sort(reverse=True)
print(f"Sort in a Descending Order {lst_color}")