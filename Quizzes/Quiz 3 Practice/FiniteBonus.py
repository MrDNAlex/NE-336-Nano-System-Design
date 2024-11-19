import numpy as np
import matplotlib.pyplot as plt

# Define Number of Internal Nodes
n = 10 # Internal Nodes

# Define X Max and Min
xMax = 10
xMin = 0

# Calculate Dx
dx = (xMax - xMin)/(n+1)

# Generate x 
x = np.linspace(xMin, xMax, n)

print(x)

# Define the D Variable for the Diagonal
D = [1/dx**2 + (dx*i)/(2*dx) for i in range(1, n)]

# Define E Variable for the Diagonal
E = -(2/dx**2)-10

# Define F Variable for the Diagonal
F = (1/dx**2 - 1/(2*dx))

# Build A Matrix
A = np.diag(np.ones(n) * E) + np.diag(D, 1) + np.diag(np.ones(n-1) * F, -1)

# Make Boundary Condition Adjustments
A[0, 0] += F

A[-1, -1] += 20*dx
A[-1, -2] += 1

# Build b Vector
b = np.ones(n)

# Define Boundary Conditions
b[0] = 40*dx*F
b[-1] = 10*dx*(1/dx**2 + (10)/(2*dx))

# Solve the Matrix
sol = np.linalg.solve(A, b)


# Plot 
plt.figure()
plt.plot(x, sol, "--")
plt.show()
