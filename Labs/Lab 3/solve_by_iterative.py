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
n = 4
m = 4
totalNodes = n * m

# Define Array of Temp
temp = [0, 25, 50, 75, 100]

# Define T Matrix
T = np.ones((n+1, m+1))

# Apply the Boundary Values
for i in range(len(temp)):
    T[0, :] = temp
    T[::-1, -1] = temp
    
# Define a Counter for Max Iterations and the Error Matrix, Max Iterations alowed, a tolerance and a lamda for relaxation
maxIter = 100
k = 0
eps = 100 * np.ones(T.shape)
tol = 1 * 10**-8
lam = 1.1

# Iterate over Solving
while k < maxIter and np.max(eps[1:, :-1]) > tol:
    for row in range(n, 0, -1):
        for col in range(0, m):
            
            # Store/Save the Previous Value
            oldVal = T[row, col]

            # Cover the Appropriate Cases
            if row == n and col == 0:  # Bottom Left Corner
                T[row, col] = 0.25 * (2 * T[row - 1, col]+ 2 * T[row, col + 1])
            elif row == n: # Bottom Side
                T[row, col] = 0.25*(2*T[row - 1, col] + T[row, col+1] + T[row, col-1])
            elif col == 0: # Left Side
                T[row, col] = 0.25*(T[row + 1, col] + T[row - 1, col] + 2*T[row, col+1])
            else: # Generic Node
                T[row, col] = 0.25 * (T[row - 1, col] + T[row + 1, col]+ T[row, col - 1]+ T[row, col + 1])
                
            # Apply some Relaxation
            T[row, col] = lam * T[row, col] + (1 - lam) * oldVal

            # Update the Error Matrix
            eps[row, col] = np.abs((T[row, col] - oldVal) / T[row, col])
            
    k += 1
    
print(T)

plt.matshow(T)
plt.title("Solution of the System Using Iterative Method")
plt.show()