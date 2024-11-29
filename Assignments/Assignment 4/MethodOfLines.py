# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
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
UInit = np.zeros(n)

# Define Lambda
lam = 1/(dr**2)

#Using t instead of z
# Define dt the Start, End and Number of Time Nodes, and create the array of Values
dt = 0.01 
tInit = 0
tEnd = 1.0
tNodes = int((tEnd - tInit)/dt + 1)
tVals = np.linspace(tInit, tEnd, tNodes)

# Define the dUdt System of Equations
def dUdt (t, U):
    
    # Stack the Right Boundary Condition
    UAll = np.hstack([U, URight])
    
    # Create the dU Vector
    dU = np.zeros(n)
    
    # Apply First Equation (Insulated Boundary)
    dU[0] = 2*UAll[1] - 2*UAll[0]
    
    # Apply all Generic Nodes
    for i in range(1, n):
        # Extract the R Value
        ri = rVals[i]
        
        # Apply Generic Node Equation
        dU[i] = (1 + dr/(2 * ri)) * UAll[i + 1] - 2*UAll[i] + (1 - dr/(2 * ri)) * UAll[i - 1]
    
    # Apply Last Node
    #dU[-1] = -2*UAll[-2] + (1-dr/(2*rVals[-2])) * UAll[-3] + (1 + dr/(2*rVals[-2]))
    
    #print(dU)
    # Return result Multiplied by Lambda
    return lam * dU
    

# Solve the System of Equations
solution = solve_ivp(dUdt, (tInit, tEnd),UInit, t_eval=tVals)

# Add the Right most Node to the System, and combine into one Matrix
sol = np.vstack([solution.y, np.ones(tNodes) * URight])

# Create Single Plot for Last Line
plt.figure(figsize=(16, 10))

# Plot the Last instance of the Graph
plt.plot(rVals, sol[:, -1], "-", label = f"Time = {tVals[-1]}")

# Add legend, labels, and show the plot
plt.legend()
plt.xlabel("Radius of the Rod (m)")
plt.ylabel("Heat of the Rod")
plt.title(f"Distribution of Heat in a Circular Rod (Method of Lines) (dt=dz={dt}) (dr={dr})")
plt.savefig(f"MethodOfLinesSingle_{dt}_{dr}.png")
plt.show()

# Create a single figure
plt.figure(figsize=(16, 10))

# Calculate 10 evenly spaced indices between the second and second-to-last
indices = np.linspace(1, tNodes - 2, 10, dtype=int)

# Plot every 10th Instance
for i in indices:
    plt.plot(rVals, sol[:, i], "--", label = f"Time = {tVals[i]:.1f}")

# Plot the Last instance of the Graph
plt.plot(rVals, sol[:, -1], "-", label = f"Time = {tVals[-1]}")

# Add legend, labels, and show the plot
plt.legend()
plt.xlabel("Radius of the Rod (m)")
plt.ylabel("Heat of the Rod")
plt.title(f"Distribution of Heat in a Circular Rod (Method of Lines) (dt=dz={dt}) (dr={dr})")
plt.savefig(f"MethodOfLines_{dt}_{dr}.png")
plt.show()