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

# Number of Internal Nodes (4 + 1 (Derivative BC))
n = 5

# Define the Right Boundary
URight = 1
UInit = 0

# Define dr the Start, End and Number of Space Nodes, and create the array of Values
dr = 0.2
rInit = 0
rEnd = 1
rNodes = int((rEnd - rInit)/dr + 1)
rVals = np.linspace(rInit, rEnd, rNodes)

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


rVals[0] = 0.1
#
# Build the A Matrix
#

# Define D as a Vector for U_i+1 and  Apply the Derivative Boundary Conidition
D = np.ones(n - 1) * -lam*(1 + dr/(2*rVals[:-2]))
D[0] = -2*lam

# Define E as Vector for U_i-1
E = np.ones(n - 1) * -lam*(1 - dr/(2*rVals[1:-1]))

# Combine all 3 Into A Matrix
A = np.diag(np.ones(n) * (1 + 2*lam)) + np.diag(D, 1) + np.diag(E, -1)

# Use LU Decomposition
LU, PIV = lu_factor(A)

# Start the Plot at 
plt.figure(figsize=(16, 10))
plt.plot(rVals, U[0, :], "--", label=f"Time = {tVals[0]}")

for l in range(tNodes - 1):
    
    # Create the b Vector
    b = np.zeros(n)
    
    # Set r0 to 0.1 to avoid Division by 0
    r0 = 0.1
    
    # Apply Both Boundary Conditions
    b[0] = 2*lam*(1 + dr/(2*r0)) * U[l, 1] + (1 - 2*lam - lam*(dr/r0)) * U[l, 0]
    b[-1] = (1 - 2*lam - lam*dr/rVals[-2]) * U[l, -2] + lam*(1 + dr/(2*rVals[-2])) * U[l, -3] + 2*lam*(1 + dr/(2*rVals[-2])) * URight
    
    for i in range(1, rNodes - 2):
        # Grab the R Value
        ri = rVals[i]
        
        # Apply Generic Node Equation
        b[i] = lam*(1 + dr/(2*ri)) * U[l, i + 1] + (1 - 2*lam - lam*dr/ri) * U[l, i] + lam*(1 + dr/(2*ri)) * U[l, i - 1]
    
    
    
    
    #for i in range(rNodes - 1):
    #    print(i)
    #    
    #    # Grab the R Value
    #    ri = rVals[i]
    #    
    #    # Avoid Division by zero, set R to something small 
    #    if ri == 0:
    #        ri = 0.1
    #    
    #    # Apply Insulated Boundary
    #    if i == 0:
    #        b[i] = 2*lam*(1 + dr/(2*ri)) * U[l, i + 1] + (1 - 2*lam - lam*(dr/ri)) * U[l, i]
    #        
    #    # Apply Right Boundary
    #    elif i == (rNodes - 2):
    #        b[i] = (1 - 2*lam - lam*dr/ri) * U[l, i] + lam*(1 + dr/(2*ri)) * U[l, i - 1] + 2*lam*(1 + dr/(2*ri)) * URight
    #    
    #    # Apply Generic Node
    #    else:
    #        b[i] = lam*(1 + dr/(2*ri)) * U[l, i + 1] + (1 - 2*lam - lam*dr/ri) * U[l, i] + lam*(1 + dr/(2*ri)) * U[l, i - 1]
    
    # Paste the Solution into the U Matrix
    U[l + 1, :-1] = lu_solve((LU, PIV), b)
    
    # Get the Time in a Good format
    time = float(int(tVals[l + 1] * 10)/10)
    
    # Determine the Plot Identifier
    if time == tEnd:
        identifier = "r-"
    else:
        identifier = "--"
    
    # Plot the Line at that time 
    plt.plot(rVals, U[l + 1, :], identifier, label=f"Time = {time}")

# Show the Plot
plt.legend()
plt.xlabel("Radius of Rod (m)")
plt.ylabel("Heat of the Rod")
plt.title("Distribution of Heat in a Circular Rod")
plt.savefig("CrankNicholson.png")
plt.show()