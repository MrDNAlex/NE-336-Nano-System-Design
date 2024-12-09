from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define the number of nodes
n = 1000

# Define the Values and initial values
k = 0.001
D = 1.2*10**(-9)
Ca0 = 0.2

# Define x Span
x0 = 0
xEnd = 0.001

# Define XVector and Y Matrix
xVals = np.linspace(x0, xEnd, n)
CaVals = np.zeros((2, xVals.size))

# Define the Function
def dfdx (t, f):
    # Unpack
    [Ca, u] = f
    return [u, (k*Ca)/D]

# Define the Boundary Condition
def BCs (fa, fb):
    
    BC1 = fa[0] - Ca0
    BC2 = fb[1]
    
    return [BC1, BC2]

# Solve the Solution
solution = solve_bvp(dfdx, BCs, xVals, CaVals)

# Extract the Solution
CaSol = solution.y[0]

# Plot
plt.figure(figsize=(16, 10))
plt.plot(xVals, CaSol, label="BVP")

#
# IVp Solution
#

# Create the Solver function
# Use Solve IVP to solve for the uValue
# Return the index to get Dy/dx [i, j] i = 1 for derivative (since u = dy/dx) j = -1 because the boundary condition is at the end
def Solver (uGuess):
    
    yGuess = solve_ivp(dfdx, (x0, xEnd), [Ca0, uGuess[0]])
    
    # Return result as Residual (yGuess - 0)
    return yGuess.y[1, -1]

# Define the Initial guess (use the solution)
uGuess = [solution.y[1, -1]] 

# Use FSolve to optimize the uValue boundary
uVal = fsolve(Solver, uGuess)

# Finally use fSolve for real
solIVP = solve_ivp(dfdx, [x0, xEnd], [Ca0, uVal[0]], t_eval=xVals)

# Plot the solution
plt.plot(xVals, solIVP.y[0], "--", label="IVP")
plt.legend()
plt.show()