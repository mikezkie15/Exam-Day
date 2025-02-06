# Generate number from 10 to 1
# decreasing step by 4
# with their square and cube and their addition of square and cube

print("Number \t\t" + "Square \t\t" + "Cube \t\t" + "Addition \t\t" )
for i in range(10,0,-4):
    print(str(i) + "   \t\t" + str(i **2)  + "    \t\t" + str(i **3) + "   \t\t" + str((i **2)+(i **3)))