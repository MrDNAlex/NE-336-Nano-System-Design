# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define the Number of Nodes (n = x, m = y)
n = 3
m = 3
totalNodes = n * m
dx = dy = 0.1

# Define the Boundary Condition Values
T_left = 50
T_bottom = 20

#
#
# Solving for Sigma = 0
#
#

#
# Start Building the frame of the A Matrix
#

# Define the Middle Diagonal
Amid = np.diag((-4) * np.ones(totalNodes))

# Define the Diagonal 1 below and above
Au1 = np.diag(np.ones(totalNodes - 1), 1)
Ab1 = np.diag(np.ones(totalNodes - 1), -1)

# Define the Diagonal 3 Below and Under
Au3 = np.diag(np.ones(totalNodes - 3), 3)
Ab3 = np.diag(np.ones(totalNodes - 3), -3)

# Add Up everything
A = Amid + Au1 + Ab1 + Au3 + Ab3

# Make Appropriate Modifications due to Boundaries
for i in range(3):
    # Apply the Top Boundary Condition
    A[6 + i, 3 + i] = 2

    # Apply The Right Boundary Condition
    A[2 + i * n, 1 + i * m] = 2

# Leftovers from Boundary Conditions
for i in range(2):
    A[3 + i * n, 2 + i * n] = 0
    A[2 + i * n, 3 + i * n] = 0

#
# Make the B Vector
#

# Empty b Vector
b = np.zeros(totalNodes)

# Apply Boundary Conditions
b[:n] -= T_bottom
b[::m] -= T_left

# Solve the Matrix
TSol = np.linalg.solve(A, b)

# Create empty T Matrix
T = np.zeros((4, 4))

# Apply Boundary Conditions
T[:, 0] = T_left
T[-1, :] = T_bottom

# Paste the Solution into the Matrix
T[2, 1:] = TSol[:n]
T[1, 1:] = TSol[n : 2 * n]
T[0, 1:] = TSol[2 * n : 3 * n]

# Display the Solution
print("\nSigma = 0 Solution")
print(T)

#
#
# Solviong for Sigma = 1*10^-4
#
#

# Define Unique values for this instance of the problem
sigma = 1 * 10**-4
Ta = 25

# Create empty T Matrix
T = np.zeros((4, 4))

# Apply Boundary Conditions
T[:, 0] = T_left
T[-1, :] = T_bottom

# Define a Counter for Max Iterations and the Error Matrix, Max Iterations alowed, a tolerance and a lamda for relaxation
maxIter = 100
k = 0
eps = 100 * np.ones(T.shape)
tol = 1 * 10**-8
lam = 1.1

# Iterate over Solving
while k < maxIter and np.max(eps[:-1, 1:]) > tol:
    for row in range(n - 1, -1, -1):
        for col in range(1, m + 1):

            # Store/Save the Previous Value
            oldVal = T[row, col]
            
            # Cover the Appriate Cases
            if row == 0 and col == m:  # Top Right Corner
                T[row, col] = 0.25 * (2 * T[row + 1, col]+ 2 * T[row, col - 1]+ dx**2 * sigma * (Ta - T[row, col] ** 4))
            elif row == 0:  # Top Side
                T[row, col] = 0.25 * (2 * T[row + 1, col]+ T[row, col + 1]+T[row, col - 1]+ dx**2 * sigma * (Ta - T[row, col] ** 4))
            elif col == m:  # Right Side
                T[row, col] = 0.25 * (2 * T[row, col - 1] + T[row + 1, col] + T[row - 1, col] + dx**2 * sigma * (Ta - T[row, col] ** 4))
            else:  # Any other case
                T[row, col] = 0.25 * (T[row - 1, col] + T[row + 1, col]+ T[row, col - 1]+ T[row, col - 1]+ dx**2 * sigma * (Ta - T[row, col] ** 4))

            # Apply some Relaxation
            T[row, col] = lam * T[row, col] + (1 - lam) * oldVal

            # Update the Error Matrix
            eps[row, col] = np.abs((T[row, col] - oldVal) / T[row, col])
    k += 1

# Display the Resulting Solution
print("\nSigma = 1-e4 Solution")
print(T)