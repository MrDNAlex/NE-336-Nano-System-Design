# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# The Only uGuess that works is -0.001, which then converges to -0.00255, anything else does not converge properly

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
plt.figure()
plt.plot(solBVP.x, CaValsBVP, "b-", label="BVP")
plt.plot(solIVP.t, CaValsIVP, "r--" , label="IVP")
plt.xlabel("Distance into the Pore (cm)")
plt.ylabel("Concentration of Species A (mol/cm^3)")
plt.title("Solution to the Concentration of Species A diffused in a Cylindrical Pore")

# Define Variables and Constants
k = 10 #cm^3 / (mol * s)
Da = 1 * 10**(-3) #cm^2/s
Ca0 = 1 * 10**(-3) # mol/cm^3

# Define the Span of X
xInit = 0
xEnd = 1.0 # cm

# Define the Number of Points and the Solution Vector
n = 10
C = np.ones(n) * Ca0
x = np.linspace(0, 1, n)

# Apply Boundary Condition
#C[0] = Ca0

# Define Delta X
dx = (xEnd - xInit)/(n-1)

# Make the A Matrices
# Middle Row
Amid = np.diag(-2*np.ones(n-1))

# Upper row
Aup = np.diag(np.ones(n-2), 1)

# Lower Row
low = np.ones(n-2)
low[-1] = 2
Alow = np.diag(low, -1)

# Combine All Rows
A = Amid + Alow + Aup

print(A)

for i in range(10):

    # Temporarily Display the Results
    #print(A)

    # Create the b Vector
    b = (np.ones(n-1)) * ((k * dx**2)/Da)*(C[1:]**2)

    b[0] -= Ca0

    Cnew = np.linalg.solve(A, b)
    print(Cnew)
    
    C[1:] = np.copy(Cnew)
    
    
    plt.plot(x, C, label=f"iter = {i}")
    

plt.legend()
plt.show()

print("\n")
print(C)
