#get six number the user
#store and display in a tuple
#clear the tuple
#display the updated tuple


numbers = []    #store the list of a number
for i in range(6):
   numbers.append(int(input("Enter 6 numbers: "))) #add the number into the list

numbers_tuple = tuple(numbers) #convert the list into tuple

print(numbers_tuple) #display the data inside the tuple

numbers_list = list(numbers_tuple) #convert the tuple into a lsit

numbers_list.clear() #use .clear() method to clear the list

tuples = tuple(numbers_list) #convert back the list into tuple
print(tuples) #display the updated tuple 

