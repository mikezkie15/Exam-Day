contact = 932737
user_info = {
    "name":"Mike Sordilla",
    "adress":"Diwan",
    "contact":contact}
print("User info")
print(user_info)
user_info.update({"contact":str(input("Update Contact: "))})
print("Updated Contact")
print(user_info)