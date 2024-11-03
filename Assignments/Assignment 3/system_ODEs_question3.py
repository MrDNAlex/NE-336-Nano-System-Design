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
k = 10 #cm^3 / (mol * s)
Da = 1 * 10**(-3) #cm^2/s
Ca0 = 1 * 10**(-3) # mol/cm^3

# Define the Span of X
xInit = 0
xEnd = 1.0 # cm

# Define the Number of Points and the Solution Vector
n = 100
x = np.linspace(0, 1, n)

# Define dx
dx = (xEnd - xInit)/(n-1)

# Create an Initial Guess Vector
Cguess = np.ones(n) * Ca0

def Matrix (CAs):
    
    # Initialize the System of Equations
    system = np.zeros(n)
    
    # Apply first Boundary Conditions
    system[0] = CAs[0] - Ca0
    
    # Iterate over the Internal Nodes
    for i in range(1, n-1):
        system[i] = CAs[i+1] - 2*CAs[i] + CAs[i-1] - ((k*dx**2)/Da)*(CAs[i]**2)
    
    # Apply Second Boundary Condition
    system[n-1] = 2*CAs[i-1] - 2*CAs[i] - ((k*dx**2)/Da)*(CAs[i]**2)
    
    # Return the System of Equations
    return system
    
# Use FSolve to solve the System
sol = fsolve(Matrix, Cguess)


#
#
# Copy Paste of the Question 2 Solution
#
#

# Define Variables and Constants
k = 10 #cm^3 / (mol * s)
Da = 1 * 10**(-3) #cm^2/s
Ca0 = 1 * 10**(-3) # mol/cm^3

# Define the Span of X
xInit = 0
xEnd = 1.0 # cm

# Define the Number of Points and the Arrays
n = 100
xVals = np.linspace(xInit, xEnd, n)
yVals = np.zeros((2, xVals.size))

# Define the Differential Function
def dfdx (x, f):
    # Decompose f into System of Equations
    [Ca, u] = f
    
    # Return the System
    return [u, 
            (k*Ca**2)/Da]

#
# Solve BVP Method
#

# Define the Boundary Conditions
def BCs (fa, fb):
    
    # Define the First Boundary Condition (Ca(0) = Ca0)
    BC1 = fa[0] - Ca0
    
    # Define the Second Boundary Condition (dCa/dx (L) = 0)
    BC2 = fb[1]
    
    return [BC1,BC2]

# Solve using the BVP Method
solBVP = solve_bvp(dfdx, BCs, xVals, yVals)

# Extract the Solution
CaValsBVP = solBVP.y[0]

#
# Solve IVP Method
#

# Use Shooting Method Solver
def Solver (uGuess):
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
# Plot the Results
#
plt.figure(figsize=(18, 12))
plt.plot(solBVP.x, CaValsBVP, "b-", label="BVP")
plt.plot(solIVP.t, CaValsIVP, "r--" , label="IVP")
plt.xlabel("Distance into the Pore (cm)")
plt.ylabel("Concentration of Species A (mol/cm^3)")
plt.title("Solution to the Concentration of Species A diffused in a Cylindrical Pore")
plt.plot(x, sol, "o", label="Finite Difference")
plt.legend()
plt.savefig("Q3_FiniteDiff_Graph")
plt.show()
