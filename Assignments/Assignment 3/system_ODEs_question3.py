# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

#
# Finite Difference Method
#

# Define Variables and Constants
k = 10  # cm^3 / (mol * s)
Da = 1 * 10 ** (-3)  # cm^2/s
Ca0 = 1 * 10 ** (-3)  # mol/cm^3

# Define the Span of X
xInit = 0
xEnd = 1.0  # cm

# Define Number of Points
n = 500
x = np.linspace(xInit, xEnd, n)

# Define dx
dx = (xEnd - xInit) / (n - 1)

# Create an Initial Guess Vector
Cguess = np.ones(n) * Ca0

# Define a Function representing the System of Equations
def Matrix(CAs, n, dx):

    # Initialize the System of Equations
    system = np.zeros(n)

    # Apply first Boundary Conditions
    system[0] = CAs[0] - Ca0

    # Iterate over the Internal Nodes
    for i in range(1, n - 1):
        system[i] = (CAs[i + 1] - 2 * CAs[i] + CAs[i - 1] - ((k * dx**2) / Da) * (CAs[i] ** 2))

    # Apply Second Boundary Condition
    system[n - 1] = 2 * CAs[i - 1] - 2 * CAs[i] - ((k * dx**2) / Da) * (CAs[i] ** 2)

    # Return the System of Equations
    return system

# Define a Function that solves Finite Differences with Varying n Value
def SolveFiniteDiff (n):
    # Define Number of Points
    x = np.linspace(xInit, xEnd, n)

    # Define dx
    dx = (xEnd - xInit) / (n - 1)

    # Create an Initial Guess Vector
    Cguess = np.ones(n) * Ca0
    
    Sol = fsolve(Matrix, Cguess, args=(n, dx))
    
    return [Sol, x]

#finDifSol = fsolve(Matrix, Cguess, args=(n, dx))
[finDifSol, x] = SolveFiniteDiff(n)

#
#
# Checking the convergence Method
#
#

# ii) 
# We can know that the solution has converged by increasing/doubling the number of nodes to be solved for in the finite difference method, and if error 
# between the previous iteration and the current is close, we know we have converged upon a solution

# Create a new Figure
plt.figure(figsize=(18, 12))

# Define the Number of Points and the Solution Vector
nConv = 5

# Define the Error Tolerance
tol = 1*10**-3

# Solve first Iteration
[prevSol, prevX] = SolveFiniteDiff(nConv)

# Plot the First Iteration
plt.plot(prevX, prevSol, "--", label="Iter = 0")

# Iterate through multiple Points
for i in range(1, 10):
    
    # Double the Number of Points
    nConv = nConv*2
    
    # Solve for the Doubled System
    [newSol, xConv] = SolveFiniteDiff(nConv)
    
    # Plot our New Iteration
    plt.plot(xConv, newSol, "--", label=f"Iter = {i}")

    # Interpolate the number of Points so that we can compare to the new solution
    inter = np.interp(xConv, prevX, prevSol)
    
    # Get the Error, if Max Error is below thershold we can break out of Loop
    if np.max(np.abs((newSol - inter)/newSol)) < tol:
        break
    
    # Save the new Solution as the Previous Values
    prevX = xConv
    prevSol = newSol

# Show the Plot
plt.legend()
plt.title("Visual Display of Finite Difference Convergence")
plt.xlabel("Distance into the Pore (cm)")
plt.ylabel("Concentration of Species A (mol/cm^3)")
plt.savefig("Q3_Convergence.png")
plt.show()

#
#
# Copy Paste of the Question 2 Solution (for comparing)
#
#

# Define Variables and Constants
k = 10  # cm^3 / (mol * s)
Da = 1 * 10 ** (-3)  # cm^2/s
Ca0 = 1 * 10 ** (-3)  # mol/cm^3

# Define the Span of X
xInit = 0
xEnd = 1.0  # cm

# Define the Number of Points and the Arrays
n = 100
xVals = np.linspace(xInit, xEnd, n)
yVals = np.zeros((2, xVals.size))

# Define the Differential Function
def dfdx(x, f):
    # Decompose f into System of Equations
    [Ca, u] = f

    # Return the System
    return [u, (k * Ca**2) / Da]

#
# Solve BVP Method
#

# Define the Boundary Conditions
def BCs(fa, fb):

    # Define the First Boundary Condition (Ca(0) = Ca0)
    BC1 = fa[0] - Ca0

    # Define the Second Boundary Condition (dCa/dx (L) = 0)
    BC2 = fb[1]

    return [BC1, BC2]


# Solve using the BVP Method
solBVP = solve_bvp(dfdx, BCs, xVals, yVals)

# Extract the Solution
CaValsBVP = solBVP.y[0]

#
# Solve IVP Method
#

# Use Shooting Method Solver
def Solver(uGuess):
    # Define the Boundaries
    CaInit = Ca0

    # Solve for the Guess Using uGuess
    yGuess = solve_ivp(dfdx, (xInit, xEnd), [CaInit, uGuess[0]])

    # Return the Last Value that we Are trying to solve for
    return yGuess.y[1, -1]

# Make an Initial Guess (Magic Number)
uGuessInit = [-0.001]

# Solve for the Correct U
correctU = fsolve(Solver, uGuessInit)

# Define the Initial Conditions
InitConditions = [Ca0, correctU[0]]

# Solve using IVP
solIVP = solve_ivp(dfdx, (0, 1), [Ca0, correctU[0]], t_eval=xVals)

# Extract the Y Data
CaValsIVP = solIVP.y[0]

#
# Plot the Results (iii)
#
plt.figure(figsize=(18, 12))
plt.plot(x, finDifSol, "o", label="Finite Difference")
plt.plot(solBVP.x, CaValsBVP, "b-", label="BVP")
plt.plot(solIVP.t, CaValsIVP, "r--", label="IVP")
plt.xlabel("Distance into the Pore (cm)")
plt.ylabel("Concentration of Species A (mol/cm^3)")
plt.title("Solution to the Concentration of Species A diffused in a Cylindrical Pore")
plt.legend()
plt.savefig("Q3_FiniteDiff_Graph")
plt.show()