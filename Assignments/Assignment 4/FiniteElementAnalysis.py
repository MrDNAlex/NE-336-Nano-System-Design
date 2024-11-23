# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

TReal = lambda x: -(15/2)*x**2 + 82.5*x + 75

# Number of internal Nodes
n = 3

# Define the Start and End Temperature
TEnd = 150
TInit = 75

# Define X
xInit = 0
xEnd = 10
xVals = np.linspace(xInit, xEnd, n + 2)

# Create the A Matrix
A = np.diag(np.ones(n) * 0.8) + np.diag(np.ones(n-1) * -0.4, 1) +  np.diag(np.ones(n-1) * -0.4, -1)

# Create the b Vector
b = np.ones(n) * 37.5

# Apply Boundary Conditions
b[0] += TInit*0.4
b[-1] += TEnd*0.4

# Solve the System of Equations
sol = np.linalg.solve(A, b)

# Add the Initial and End Value to the Array
fullSolution = np.hstack([TInit, sol, TEnd])

# Display the Solution
print("\n\nT Distribution = ", fullSolution)

# Define More detailed points for Real Solution
xVals2 = np.linspace(xInit, xEnd, 1000)

# Plot the Comparison
plt.figure(figsize=(16, 10))
plt.title("Comparison of Analytical Solution and Finite Element Analysis Solution")
plt.xlabel("Distance (m)")
plt.ylabel("Temperature (Celsius)")
plt.plot(xVals2, TReal(xVals2), label="Real Solution")
plt.plot(xVals, fullSolution, label="Finite Element")
plt.legend()
plt.savefig("FiniteElementAnalysis.png")
plt.show()