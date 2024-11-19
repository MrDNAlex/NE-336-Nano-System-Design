#Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

from scipy.optimize import newton

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Notes : Proper Uguess is -0.00255 (If I don't have a uGuess anywhere near that I can't get a valid solution)

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
    #yGuess = solve_ivp(dfdx, (xInit, xEnd), [CaInit, uGuess[0]])
    
    yGuess = solve_ivp(dfdx, (xInit, xEnd), [CaInit, uGuess[0]], t_eval=xVals, method="RK45")
    
    # Return the Last Value that we Are trying to solve for
    return yGuess.y[1, -1]

# 
# Make an Initial Guess (Magic Number)
#uGuessInit = [-0.001]

guesses = np.linspace(-1, 1, 1000)

for i in iter(guesses):
    uGuessInit = [i]
    
    # Solve for the Correct U
    correctU = fsolve(Solver, uGuessInit)
    #correctU = fsolve(Solver, uGuessInit, xtol=10**(-12))

    # Define the Initial Conditions
    InitConditions = [Ca0, correctU[0]]

    # Solve using IVP
    #solIVP = solve_ivp(dfdx, (0, 1), [Ca0, correctU[0]], t_eval=xVals)
    solIVP = solve_ivp(dfdx, (xInit, xEnd), InitConditions, t_eval=xVals, method="RK45")
    
    CaValsIVP = np.interp(xVals, solIVP.t, solIVP.y[0])
    #CaValsIVP = solIVP.y[0]
    
    if (abs(sum(CaValsBVP - CaValsIVP)) < 0.01):
        print(f"Valid UGuess : {i}  --> Correct U = {correctU}")
        print()
        


#
# Plot the Results
#

plt.figure()
plt.plot(solBVP.x, CaValsBVP, "b-", label="BVP")
plt.plot(solIVP.t, CaValsIVP, "r--" , label="IVP")
plt.legend()
plt.show()