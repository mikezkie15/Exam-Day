#Get 6 number from user
#store number in a tupel
#sum the total number and display

#store the number in a list
numbers = []


for i in range(6): #use to get user number six times
    numbers.append(float(input("Enter 6 number: "))) #store number in the list
 
numbers_tuple = tuple(numbers) #convert list into tuple data type


sum = 0 #variable to store the total sum
for i in numbers_tuple:
    sum += i #add the number a numbER from the tuples every single iteration

print(type(numbers_tuple))
print("The total sum of the number is: " + str(sum))