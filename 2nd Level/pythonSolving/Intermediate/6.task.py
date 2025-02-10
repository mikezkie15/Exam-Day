# Create a dictionay
# find the total length of key and value in a dictionary

student_dic = {"name":"Mike","last_name":"Sordilla"}
total_key_length = sum(len(k) for k in student_dic.keys())
total_value_length = sum(len(str(i)) for i in student_dic.values())
print(f"The total length of keys is {total_key_length}")
print(f"The total length of value is {total_value_length}")

value_length = 0
for l in student_dic.keys():
    if l == 0:
        print("No Value")
    else:
        value_length = len(l) 
print(f"Total value is {value_length}")