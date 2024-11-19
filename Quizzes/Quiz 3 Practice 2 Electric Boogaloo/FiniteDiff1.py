import numpy as np
import matplotlib.pyplot as plt
 
# Number of Internal Nodes
n = 20

# Define the X Max and X Min
xMin = 0
xMax = 10

# Define yInit and yEnd
yInit = 20
yEnd = 10

# Define the X Vector
x = np.linspace(xMin, xMax, n+2)

# Define dx
dx = (xMax - xMin)/(n + 1)

# Create the D and E Variable which are for the i+1 and i-1 on the diagonals
D = np.ones(n-1) * (1/dx**2 + x[1:-2]/(2*dx))
E = np.ones(n-1) * (1/dx**2 - x[2:-1]/(2*dx))

# Make the A matrix
A = np.diag(np.ones(n) * (-(2/dx**2) - 10)) + np.diag(D, 1) + np.diag(E, -1)

# Make the b Vector
b = np.zeros(n)

# Apply Boundary Conditions
b[0] += -yInit* (1/dx**2 - x[1]/(2*dx))
b[-1] += -yEnd * (1/dx**2 + x[-2]/(2*dx))

# Solve the Matrix
sol = np.linalg.solve(A, b)

# Define the y Vector
y = np.zeros(n + 2)

# Apply the Inital and End Value
y[0] = yInit
y[-1] = yEnd

# Input the Solution
y[1:-1] = sol

# Plot the Solution
plt.figure()
plt.plot(x, y, "--")
plt.show()