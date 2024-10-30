# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:12:30 2024

@author: a3dufres
"""
# Imports
from scipy.integrate import solve_ivp, solve_bvp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve


#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define the Function
def dfdr (r, f):
    [T, u] = f
    
    return [u, -(1/r)*u]

# Define the Boundary Condition Function
def BCs (fa, fb):
    
    # BC 1 (T(r=5)=20)
    BC1 = fa[0] - 20
    
    # BC 2 (DT/dr(r=10) = 10)
    BC2 = fb[1] - 10
    
    return [BC1, BC2]

# Define the Bounds of r
(r0, rend) = (5, 10)

# Define the Number of Points to Graph
n = 300

# Define the list of Points for R
rVals = np.linspace(r0, rend, n)

# Define the Points for y Vals
yVals = np.zeros((2, rVals.size))

# Solve using BVP
sol = solve_bvp(dfdr, BCs, rVals, yVals)

# Plot the Figure
plt.figure()
plt.plot(rVals, sol.y[0], label="BVP Solution")
plt.title("The Temperature Distribution in the Annular Cylinder")
plt.xlabel("Radius (r)")
plt.ylabel("Temperature (T)")
plt.legend()

# Bonus Shooting Method

#
# IVP Method
#

# Define the Boundary Conditions
TInit = 20
TFinal = 10

# Use Shooting Method
def Solve (uGuess):
    TGuess = solve_ivp(dfdr, (r0, rend), [TInit, uGuess[0]])
    return TGuess.y[1, -1]-TFinal

# Make an Initial guess for U
uGuess1 = [10]

# Solve for the Correct U Value
correctU = fsolve(Solve, uGuess1)

# Create Initial Condition
InitCond = [TInit, correctU[0]]

#Solve for the IVP
TIVP = solve_ivp(dfdr, (r0, rend), InitCond, t_eval=rVals)

# Plot the Solution for IVP
plt.plot(rVals, TIVP.y[0], "r--", label=f"IVP Method")

# Plot again to have both on the same graph
plt.title("The Temperature Distribution in the Annular Cylinder")
plt.xlabel("Radius (r)")
plt.ylabel("Temperature (T)")
plt.legend()
plt.show()