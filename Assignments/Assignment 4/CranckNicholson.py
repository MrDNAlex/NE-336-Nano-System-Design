# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define dr the Start, End and Number of Space Nodes, and create the array of Values
dr = 0.2
rInit = 0
rEnd = 1
rNodes = int((rEnd - rInit)/dr + 1)
rVals = np.linspace(rInit, rEnd, rNodes)

# Number of Internal Nodes (4 + 1 (Derivative BC) = rNodes - 1)
n = rNodes - 1

# Define the Right Boundary
URight = 1
UInit = 0

#Using t instead of z
# Define dt the Start, End and Number of Time Nodes, and create the array of Values
dt = 0.1
tInit = 0
tEnd = 1.0
tNodes = int((tEnd - tInit)/dt + 1)
tVals = np.linspace(tInit, tEnd, tNodes)

# Define Lambda
lam = dt/(2*dr**2)

# Create the U Matrix, Define the Initial Condition and Right Boundary Condition
U = np.zeros((tNodes, rNodes))
U[0, 1:-1] = UInit
U[:, -1] = URight

#
# Build the A Matrix
#

# Define D as a Vector for U_i+1 and  Apply the Derivative Boundary Conidition
D = np.ones(n - 1) 
D[1:] *= -lam*(1 + dr/(2*rVals[1:-2]))
D[0] = -2*lam

# Define E as Vector for U_i-1
E = np.ones(n - 1) * -lam*(1 - dr/(2*rVals[1:-1]))

# Combine all 3 Into A Matrix
A = np.diag(np.ones(n) * (1 + 2*lam)) + np.diag(D, 1) + np.diag(E, -1)

# Apply Forward Difference for the Initial Node
A[0, :] = 0
A[0, 0] = 3
A[0, 1] = -4
A[0, 2] = 1

# Use LU Decomposition
LU, PIV = lu_factor(A)

# Loop through all Nodes to Solve
for l in range(tNodes - 1):
    
    # Create the b Vector
    b = np.zeros(n)
    
    # Apply Both Boundary Conditions
    b[0] = -U[l, 2] + 4*U[l, 1] - 3*U[l, 0]
    b[-1] = 2*lam*(1+dr/(2*rVals[-2])) * URight + (1 - 2*lam)*U[l, -1] + lam*(1 - dr/(2*rVals[-2]))*U[l, -2]
    
    # Set all other b Vector Values
    for i in range(1, rNodes - 2):
        # Grab the R Value
        ri = rVals[i]
        
        # Apply Generic Node Equation
        b[i] = lam*(1 + dr/(2*ri)) * U[l, i + 1] + (1 - 2*lam) * U[l, i] + lam*(1 - dr/(2*ri)) * U[l, i - 1]
    
    # Paste the Solution into the U Matrix
    U[l + 1, :-1] = lu_solve((LU, PIV), b)
    
# Plot the Single Graph

# Start the Plot
plt.figure(figsize=(16, 10))

# Plot the Last Graph with a Unique Identifier
plt.plot(rVals, U[-1, :], "-", label=f"Time = {float(int(tVals[-1] * 10)/10):.1f} s")
plt.legend()
plt.xlabel("Radius of Rod (m)")
plt.ylabel("Heat of the Rod")
plt.title(f"Distribution of Heat in a Circular Rod (Crank Nicholson) (dt=dz={dt}) (dr={dr})")
plt.savefig(f"CrankNicholsonSingle_DT_{dt}_{dr}.png")
plt.show()

# Start the Plot
plt.figure(figsize=(16, 10))

# Calculate 10 evenly spaced indices between the second and second-to-last
indices = np.linspace(1, tNodes - 2, 10, dtype=int)

# Plot All other Graphs between Second and Second Last 
for i in indices:
    plt.plot(rVals, U[i, :], "--", label=f"Time = {tVals[i]:.1f} s")
    
# Plot the Last Graph with a Unique Identifier
plt.plot(rVals, U[-1, :], "-", label=f"Time = {float(int(tVals[-1] * 10)/10):.1f} s")

# Show the Plot
plt.legend()
plt.xlabel("Radius of Rod (m)")
plt.ylabel("Heat of the Rod")
plt.title(f"Distribution of Heat in a Circular Rod (Crank Nicholson) (dt=dz={dt}) (dr={dr})")
plt.savefig(f"CrankNicholson_DT_{dt}_{dr}.png")
plt.show()