# Find the coulomb between two charges
# Get two value from the user (q1,q2) and the distance(r) in meter
# Applies the Coulomb Law formula
# Return electrrostatic force in Newtons

q1 = float(input("Enter charge 1 : "))
q2 = float(input("Enter charge 2 : "))
r = float(input("Enter the distance between the two charges: "))

k_constant = 8.99e9

Force = k_constant * (q1 * q2) / (r ** 2)

print(f"The coulomb constant force us {Force:.2f} N" )
