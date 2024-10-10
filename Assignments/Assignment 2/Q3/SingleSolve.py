#
# Gauss Siedel Method
#

# Initialize System
b = [247, 248, 239]

eq1 = [0.2425, 0, -0.9701]
eq2 = [0, 0.2425, -0.9701]
eq3 = [-0.2357, -0.2357, -0.9428]

# Initialize Initial Values
x1 = 10
x2 = 10
x3 = 10

# Loop over 10 Times
for i in range(10):
    # Apply Gauss Siedel for each equation
    x1 = (b[0] - eq1[1]*x2 - eq1[2]*x3)/eq1[0]
    x2 = (b[1] - eq2[0]*x1 - eq2[2]*x3)/eq2[1]
    x3 = (b[2] - eq3[0]*x1 - eq3[1]*x2)/eq3[2]

print("\n")
print(f"x1 : {x1}, x2 : {x2}, x3 : {x3}")
print("\n")