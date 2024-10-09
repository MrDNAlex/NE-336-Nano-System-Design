import numpy as np
from scipy.linalg import lu

# LU Decomposition
A = [[-8, 1, -2], [2, -6, -1], [-3, -1, 7]]
b = [[-20], [-38], [-34]]

# Get P L U Matrices
P, L, U = lu(A)

# Solve for d Vector
d = np.linalg.solve(L, b)

# Solve for X Solution
x_lu = np.linalg.solve(U, d)

print("\n")
print(f"Solution to the LU Decomposition is as Follows : x1 = {x_lu[0, 0]},  x2 = {x_lu[1, 0]},  x3 = {x_lu[2, 0]}")
print("\n")




#Linalg Solve Method
A = [[-8, 1, -2], [2, -6, -1], [-3, -1, 7]]
b = [[-20], [-38], [-34]]

x_sol = np.linalg.solve(A, b)

print("\n")
print(f"Solution to the Linalg.Solve method is as Follows : x1 = {x_sol[0, 0]},  x2 = {x_sol[1, 0]},  x3 = {x_sol[2, 0]}")
print("\n")




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
