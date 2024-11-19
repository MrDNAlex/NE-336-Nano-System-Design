import numpy as np
import matplotlib.pyplot as plt
 
# Number of Internal Nodes
n = 100

# Define the X Max and X Min
xMin = 0
xMax = 10

# Define yInit and yEnd
yInit = 20
yEnd = 10

# Define the X Vector
x = np.linspace(xMin, xMax, n)

# Define dx
dx = (xMax - xMin)/(n - 1)

# Create the D and E Variable which are for the i+1 and i-1 on the diagonals
D = np.ones(n-1) * (1/dx**2 + x[:-1]/(2*dx))
E = np.ones(n-1) * (1/dx**2 - x[1:]/(2*dx))

# Make the A matrix
A = np.diag(np.ones(n) * (-(2/dx**2) - 10)) + np.diag(D, 1) + np.diag(E, -1)

# Add the Extra Value for the first Equation
A[0, 1] += (1/dx**2 - x[0]/(2*dx))

# Reset the Last Row so that we can apply backwards difference
A[-1, :] = 0

# Apply Backwards Difference
A[-1, -1] += (2-20*dx)
A[-1, -2] += -4
A[-1, -3] += 1


# Make the b Vector
b = np.zeros(n)

# Apply Boundary Conditions
b[0] += 40*dx*(1/dx**2 + x[0]/(2*dx))
b[-1] += -100*dx

# Solve the Matrix
sol = np.linalg.solve(A, b)

# Plot the Solution
plt.figure()
plt.plot(x, sol, "--")
plt.show()