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
x = np.linspace(xMin, xMax, n + 2)

print(x)

# Define the D Variable for the Diagonal
D = [1/dx**2 + (dx*i)/(2*dx) for i in range(1, n)]

# Define E Variable for the Diagonal
E = -(2/dx**2)-10

# Define F Variable for the Diagonal
F = (1/dx**2 - 1/(2*dx))

# Build A Matrix
A = np.diag(np.ones(n) * E) + np.diag(D, 1) + np.diag(np.ones(n-1) * F, -1)


# Build b Vector
b = np.ones(n)

# Define Boundary Conditions
b[0] = -20*F
b[-1] = -10*(1/dx**2 + (10)/(2*dx))

# Solve the Matrix
sol = np.linalg.solve(A, b)

# Generate y Vector
y = np.zeros(n + 2)

# Apply Boundary Conditions
y[0] = 20
y[-1] = 10

# Input Solution
y[1:-1] = sol

# Plot 
plt.figure()
plt.plot(x, y, "--")
plt.show()
