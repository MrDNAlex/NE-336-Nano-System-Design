# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Constants and Variables
k = 10  # cm^3 / (mol * s)
Da = 1 * 10**(-3)  # cm^2/s
Ca0 = 1 * 10**(-3)  # mol/cm^3

# Span and points
xInit = 0
xEnd = 1.0  # cm
n = 100  # number of points
xVals = np.linspace(xInit, xEnd, n)
yVals = np.zeros((2, xVals.size))

# Differential function
def dfdx(x, f):
    Ca, u = f
    return [u, (k * Ca**2) / Da]

# Boundary conditions for BVP
def BCs(fa, fb):
    BC1 = fa[0] - Ca0  # Ca(0) = Ca0
    BC2 = fb[1]        # dCa/dx (L) = 0
    return [BC1, BC2]

# Solve the BVP
solBVP = solve_bvp(dfdx, BCs, xVals, yVals)
CaValsBVP = solBVP.y[0]  # Solution for Ca from BVP

# IVP shooting method solver
def Solver(uGuess):
    CaInit = Ca0
    yGuess = solve_ivp(dfdx, (xInit, xEnd), [CaInit, uGuess[0]], t_eval=xVals, method="RK45")
    return yGuess.y[1, -1]  # Return the final value of u

# Attempt guesses for IVP
guesses = np.linspace(-1, 1, 1000)

for i in guesses:
    uGuessInit = [i]
    correctU = fsolve(Solver, uGuessInit)

    # Initial conditions with the solved correctU
    InitConditions = [Ca0, correctU[0]]

    # Solve the IVP with t_eval=xVals to ensure it matches BVP points
    solIVP = solve_ivp(dfdx, (xInit, xEnd), InitConditions, t_eval=xVals, method="RK45")
    CaValsIVP = solIVP.y[0]

    if not len(CaValsBVP) == len(CaValsIVP):
        print("Not the Same")

    # Check for convergence within tolerance
    if len(CaValsBVP) == len(CaValsIVP) and abs(sum(CaValsBVP - CaValsIVP)) < 0.01:
        print(f"Valid UGuess : {i}")
        break  # Exit loop if solution is found

# Plot the results
plt.figure()
plt.plot(solBVP.x, CaValsBVP, "b-", label="BVP Solution")
plt.plot(solIVP.t, CaValsIVP, "r--", label="IVP Solution")
plt.xlabel("x")
plt.ylabel("Concentration Ca")
plt.legend()
plt.show()
