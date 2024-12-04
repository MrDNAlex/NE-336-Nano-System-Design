import numpy as np
from scipy.linalg import lu

# Permuted A
A_permuted = np.array([[-8, 1, -2],
                       [-3, -1, 7],
                       [2, -6, -1]], dtype=float)

# Permuted b to match A_permuted
b_permuted = np.array([[-20],
                       [-34],
                       [-38]], dtype=float)

# Perform PLU decomposition
P, L, U = lu(A_permuted)

# Adjust b according to the permutation matrix P
Pb = P @ b_permuted

# Solve Ly = Pb (forward substitution)
y = np.linalg.solve(L, Pb)

# Solve Ux = y (backward substitution)
x_lu = np.linalg.solve(U, y)

# Print the results
print("\n")
print(f"Solution to the LU Decomposition is as follows: x1 = {x_lu[0, 0]:.4f}, x2 = {x_lu[1, 0]:.4f}, x3 = {x_lu[2, 0]:.4f}")
print("\n")


import numpy as np
from scipy.linalg import lu

# Modified system: First equation moved to the end
A_modified = np.array([[-3, -1, 7],
                       [-8, 1, -2],
                       [2, -6, -1]], dtype=float)

b_modified = np.array([[-34],
                       [-20],
                       [-38]], dtype=float)

# Perform PLU decomposition
P, L, U = lu(A_modified)

# Adjust b according to the permutation matrix P
Pb = P @ b_modified

# Solve Ly = Pb (forward substitution)
y = np.linalg.solve(L, Pb)

# Solve Ux = y (backward substitution)
x_lu = np.linalg.solve(U, y)

# Print the results
print("\n")
print(f"Solution to the modified system: x1 = {x_lu[0, 0]:.4f}, x2 = {x_lu[1, 0]:.4f}, x3 = {x_lu[2, 0]:.4f}")
print("\n")
