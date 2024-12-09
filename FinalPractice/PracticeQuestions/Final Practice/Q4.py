from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define the R Equation
r = lambda x: 0.02 - 0.1*x

# Define all values and constants
h = 20
k = 14
Tair = 20
T0 = 100
L = 0.1
n = 1000

# Create the Function
def dTdx (x, f):
    [T, u] = f
    
    du = (2*h/k*(T-Tair)+0.2*u)/r(x)
    
    return [u, du]

# Create Boundary Conditions
def BCs (fa, fb):
    
    EQ1 = fa[0] - T0
    EQ2 = k*fb[1] + h * (fb[0] - Tair)
    
    return [EQ1, EQ2]

# Create xVals and YVals 
xVals = np.linspace(0, L, n)
TVals = np.zeros((2, xVals.size))

# Solve using BVP
solution = solve_bvp(dTdx, BCs, xVals, TVals)

# Extract the Solution
TSol = solution.y[0]

print("Start:", TSol[0])
print("End:", TSol[-1])

plt.figure(figsize=(16, 10))
plt.plot(xVals, TSol)
plt.plot(xVals, solution.y[1]*r(xVals)**2)
plt.show()