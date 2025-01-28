# Get 5 author Name with their Book Name
# Display last author with its Book Name

library = {}

for i in range(2):
    author_name = input("Enter author name: ")
    book_name = input("Enter Book name: ")
    library[author_name] = book_name
print("First Author is " + str(list(library.keys())[0]))
print("Bookname is " + str(list(library.values())[0]))
print(library)