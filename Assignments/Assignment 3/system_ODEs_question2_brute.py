#Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
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
    
    # Return last value
    return yGuess.y[1, -1]


def IVPMethod (uGuess):
    # Make an Initial Guess
    uGuessInit = [uGuess]
    
    # Solve for the Correct U
    correctU = fsolve(Solver, uGuessInit)

    # Define the Initial Conditions
    InitConditions = [Ca0, correctU[0]]

    # Solve using IVP
    solIVP = solve_ivp(dfdx, (xInit, xEnd), InitConditions)
    
    # Interpolate the Values so that we can directly compare
    CaValsIVP = np.interp(xVals, solIVP.t, solIVP.y[0])
    
    return [CaValsIVP, correctU]
    
# Make a List of a lot of Guesses
guesses = np.linspace(-1, 1, 1000)
validUGuess = []

# Brute force Solve for Valid U guesses
for i in guesses:
    
    # Run the Solve IVP Method
    [CaValsIVP, correctU] = IVPMethod(i)
    
    # Check if the Difference between curves are negligeable, if so print that it is a Valid uGuess, and display the CorrectU solved
    diff = abs(sum(CaValsBVP - CaValsIVP))
    if (diff < 0.1):
        validUGuess.append(i)
        print(f"\nValid UGuess : {i}  --> Correct U = {correctU} (diff = {diff})\n")

# Print the Valid range of U Guesses
print(f"Valid Range of U guesses are {min(validUGuess)} <-> {max(validUGuess)}")


plt.figure()
for i in validUGuess:
    [CaValsIVP, correctU] = IVPMethod(i)
    plt.plot(xVals, CaValsIVP, "--", label=f"IVP (u = {i})")

plt.plot(solBVP.x, CaValsBVP, "b-", label="BVP")

plt.legend()
plt.show()