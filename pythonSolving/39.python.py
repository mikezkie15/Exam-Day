# Get 5 number from the user
# store the number to a tuple
# pass into a function that multiply and add the number
# Then display the result

tpl = ()
lst = []
for i in range(5):
    lst.append(int(input("Enter a number: ")))

tpl_to_pass = tuple(lst)

def add_mul(tpl_element):
    sum = 0
    mult = 1
    for j in tpl_element:
        sum += j
        mult *= j
    print("the total sum of the tuple is " + str(sum))
    print("The incremental product of the tuple is " + str(mult))

add_mul(tpl_to_pass)