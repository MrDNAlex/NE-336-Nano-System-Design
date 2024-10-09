import numpy as np
#Inverse Method
A = [[-8, 1, -2], [2, -6, -1], [-3, -1, 7]]
b = [[-20], [-38], [-34]]

# Inverse Matrix
A_inv = np.linalg.inv(A)

# Apply Matrix Multiplication with Inverse Matrix
x_sol = A_inv @ b

print("\n")
print(f"Solution to the Inverse Matrix method is as Follows : x1 = {x_sol[0, 0]},  x2 = {x_sol[1, 0]},  x3 = {x_sol[2, 0]}")
print("\n")
