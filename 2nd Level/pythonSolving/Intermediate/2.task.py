# centegrade to f (0°C × 9/5) + 32 = 32°F
# centegrade to k 0°C + 273.15 = 273.15K

# get a userinput 
# convert c to f
# convert c to k

centegrade = float(input("Enter a number in centegrade: "))

c_to_f = (centegrade * 9/5) + 32
c_to_k = centegrade + 273.15

print(f"{centegrade}")
print(f"Centegrade is conerted into {c_to_f} frenheith")
print(f"Centegrade is conerted into {c_to_k} kelvin")
