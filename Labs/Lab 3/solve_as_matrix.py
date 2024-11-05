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

# Start Building A Matrix

# Define the Middle Diagonal
Amid = np.diag(-4*np.ones(totalNodes))

# Define Upper Diagonal
AU1 = np.ones(totalNodes-1)
AU1[::4] = 2
AU1[3::4] = 0

# Define Lower Diagonal
AD1 = np.ones(totalNodes-1)
AD1[3::4] = 0

# Define Upper 4 Diagonal
AU4 = np.ones(totalNodes-4)
AU4[:4:] = 2

# Define Lower 4 Diagonal
AD4 = np.ones(totalNodes-4)

# Sum Up all Matrices
A = Amid + np.diag(AU1, 1) + np.diag(AD1, -1) + np.diag(AU4, 4) + np.diag(AD4,-4)

print("\n")
print(A)

# Define b Vector
b = np.zeros(totalNodes)

# Fill in b Vector
for i in range(len(temp) - 1):
    b[3+i*4] -= temp[i]
    b[-4+i] -= temp[i]
  
# Define T Matrix
T = np.zeros((n+1, m+1))

# Apply the Boundary Values
for i in range(len(temp)):
    T[0, :] = temp
    T[::-1, -1] = temp

# Solve for the Solution
TSol = np.linalg.solve(A, b)

#for i in range(len(n)):
T[-1, :4] = TSol[:4]
T[-2 ,:4] = TSol[4:8]
T[-3 ,:4] = TSol[8:12]
T[-4 ,:4] = TSol[12:16]

print(T)

# Plot the End Result
plt.matshow(T)
plt.title("Solution of the System Using Matrix Method")
plt.show()