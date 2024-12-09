# Imports
from scipy.integrate import solve_ivp, solve_bvp
from scipy.optimize import fsolve
from scipy.linalg import lu_factor, lu_solve
import numpy as np
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define the Number of nodes
n = 1000

# Defining a Scaling factor to plot in Cm
ScaleCM = 100

# Rewriting the Variable to be more clean for me (Sorry)

# Define the Range of Radius
r0 = 0.05
rEnd = 0.1

# Create the rVals Vector
rVals = np.linspace(r0, rEnd, n)

# Define the Boundary Condition Values
T0 = 100
TEnd = 20

# Define the Plotting 
fig, ax1 = plt.subplots()
plt.title("Solution to the Temperature in a Annular Cylinder")
plt.xlabel("Radius of the Cylinder (cm)")
plt.ylabel("Temperature in the Cylinder (Celsius)")

# Define another Axis
ax2 = ax1.twinx()

#
# Shooting method (Solve BVP)
#

# Define the system of ODEs
def dTdr (r, f):
    
    [T, u] = f
    
    du = -u/r
    
    return [u, du]

# Define the Boundary Conditions
def BCs (fa, fb):
    
    # make the Boundaries as residuals 
    BC1 = fa[0] - T0
    BC2 = fb[0] - TEnd

    return [BC1, BC2]

# Define the initial condition of the system
Tinit = np.zeros((2, rVals.size))

# Solve using the BVP Method
solution = solve_bvp(dTdr, BCs, rVals, Tinit)

# Extract the solutions for both components
BVPSol = solution.y[0]
BVPdtSol = solution.y[1]

# Plot the Solution
ax1.plot(rVals * ScaleCM, BVPSol, label="BVP Shooting")
ax2.plot(rVals * ScaleCM, BVPdtSol, label="BVP Derivative")

#
# For fun lets solve Solve_IVP as a victory lap and (maybe offset some things I got wrong?)
#

# Create a Solver function to find the U boundary
def Solver (uGuess):
    
    # Solve for a random yGuess
    yGuess = solve_ivp(dTdr, (r0, rEnd), [T0, uGuess[0]])
    
    # Return the Residual of the Boundary
    return yGuess.y[0, -1] - TEnd


# Slope goes down initially
uGuess = [-3]

# Get the correct U value for the boundary using fsolve
uCorrect = fsolve(Solver, uGuess)

# Solve for the System using Solve IVP and our new U Value
IVPSolution = solve_ivp(dTdr, (r0, rEnd), [T0, uCorrect[0]], t_eval=rVals)

# Cache and Extract the Solutions
IVPSol = IVPSolution.y[0]
IVPdTSol = IVPSolution.y[1]

# Plot it on the Graph
ax1.plot(rVals * ScaleCM, IVPSol, "g-.", label="IVP Shooting")
ax2.plot(rVals * ScaleCM, IVPdTSol, "g-.", label="IVP Derivative")

#
# Finite Difference Method
#

# Define the number of nodes and the number of internal nodes (Feel free to crank up the number of Nodes)
n = 6
internalNodes = n - 2

# Redefine the Variables for the smaller size
rVals = np.linspace(r0, rEnd, n)
dr = (rEnd - r0)/(n-1)

#
# Build the A Matrix
#

# Define the Vectors
Amid = np.ones(internalNodes) * -2
Aup = np.ones(internalNodes - 1) * (1 + dr/(2*rVals[1:-2]))
Adown = np.ones(internalNodes - 1) * (1 - dr/(2*rVals[2:-1]))

# Combine the vectors into the final A matrix
A = np.diag(Amid) + np.diag(Aup, 1) + np.diag(Adown, -1)

# Create the b Vector
b = np.zeros(internalNodes)

# Apply the Boundary conditions
b[0] = -T0 * (1 - dr/(2*rVals[1]))
b[-1] = -TEnd * (1 + dr/(2*rVals[-2]))

# Solve the System of EQs
sol = np.linalg.solve(A, b)

# Define the final solution matrix
T = np.zeros(n)
T[0] = T0
T[-1] = TEnd
T[1:-1] = sol

# Get the Derivative
dT = np.zeros(n)

# Get the Derivatives
dT[0] = (-T[2] + 4*T[1] - 3*T[0])/(2*dr)
dT[-1] = (3*T[-1] - 4*T[-2] + T[-3])/(2*dr)
dT[1:-1] = (T[2:] - T[:-2])/(2*dr)

# Plot the Finite Differences
ax1.plot(rVals * ScaleCM, T, "r--", label="FD Method")
ax2.plot(rVals * ScaleCM, dT, "r--", label="FD Derivative")

# Don't remember what the command is for changing the axis
#ax2.ylabel("Change in Temperature in the Cylinder (Celsius)")

# Display the Legends and show
ax1.legend()
ax2.legend()
plt.show()

# Sorry if the Graph is not very easy to read, feel free to remove labels and change the markers