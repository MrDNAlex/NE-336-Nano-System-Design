#Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define the Function
def dfdt (t, f):
    [y, u] = f
    
    return [u,
            -0.1 * u - 9.81 * np.sin(y) + np.cos(t)]

# Setting up the Problem
tInit = 0
tFinal = np.pi * 2
n = 300
tVals = np.linspace(tInit, tFinal, n)
yVals = np.zeros((2, tVals.size))

# Small Fix (Pendar Suggested to Solve for Correct Root)
yVals[0]=np.pi/6

# Start Plotting
plt.figure()
plt.title("Solution to the Pendulum")

#
# IVP Method
#

# Use Shooting Method
def Solve (uGuess):
    yInit = np.pi / 6
    yFinal = np.pi / 6
    yGuess = solve_ivp(dfdt, (tInit, tFinal), [yInit, uGuess[0]])
    return yGuess.y[0, -1]-yFinal

# Make an Initial guess for U
uGuess1 = [10]

# Solve for the Correct U Value
correctU = fsolve(Solve, uGuess1)

# Create Initial Condition
InitCond = [np.pi / 6, correctU[0]]

#Solve for the IVP
YIVP = solve_ivp(dfdt, (tInit, tFinal), InitCond, t_eval=tVals)

# Plot the Solution for IVP
plt.plot(tVals, YIVP.y[0], "r-", label=f"IVP Method")


#
# BVP Method
#

# Define Boundary Condition
def BCs (ya, yb):
    yInit = np.pi / 6
    yFinal = np.pi / 6
    
    return  [ya[0] - yInit, yb[0] - yFinal]

# Solve for the 
solBVP = solve_bvp(dfdt, BCs, tVals, yVals)

# Extract Y Data
yValsBVP = solBVP.y[0]

# Plot the BVP Method
plt.plot(solBVP.x, yValsBVP, "b-", label=f"BVP Method")

#
# No Damping
#

# Define the No Damping function
def dfdt_nodamp (t, f):
    [y, u] = f
    
    return [u,
            - 9.81 * np.sin(y)]

# Solve for the No Damp Solution
solBVPNoDamp = solve_bvp(dfdt_nodamp, BCs, tVals, yVals)

# Extract Y Data
yValsBVPNoDamp = solBVPNoDamp.y[0]

# Plot the BVP Method (No Damp)
plt.plot(solBVPNoDamp.x, yValsBVPNoDamp, "g-", label=f"BVP Method (No Damp)")

# Show the Plot
plt.legend()
plt.xlabel('Time')
plt.ylabel('Position of the Pendulum')
plt.show()