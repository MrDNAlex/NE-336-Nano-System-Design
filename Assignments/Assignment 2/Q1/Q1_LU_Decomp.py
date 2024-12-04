# LU Decomposition
import numpy as np
from scipy.linalg import lu

A = [[-8, 1, -2], [2, -6, -1], [-3, -1, 7]]
b = [[-20], [-38], [-34]]

A = [ [2, -6, -1], [-3, -1, 7], [-8, 1, -2]]
b = [[-38], [-34], [-20]]

P, L, U = lu(A)

d = np.linalg.solve(L, b)

x_lu = np.linalg.solve(U, d)

print("\n")
print(f"Solution to the LU Decomposition is as Follows : x1 = {x_lu[0, 0]},  x2 = {x_lu[1, 0]},  x3 = {x_lu[2, 0]}")
print("\n")
