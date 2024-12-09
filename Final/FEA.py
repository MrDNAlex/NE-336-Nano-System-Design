# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:33:18 2024

@author: a3dufres
"""

# Imports
from scipy.integrate import solve_ivp, solve_bvp
from scipy.optimize import fsolve
from scipy.linalg import lu_factor, lu_solve
import numpy as np
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define the A Matrix
A = np.array([[-0.5, 0.5, 0], [0.5, -1, 0.5], [0, 0.5, -1 ]])

# Define the b Vector
b = [22, 20, 20]

# Solve for it
solution = np.linalg.solve(A, b)

# Define the Final T system and Paste solution into it
U = np.zeros(4)
U[-1]= 0
U[:-1] = solution

# Get the Boundary Derivatives
duEnd = -0.5 * U[2] + 10
du0 = -0.5*U[0] + 0.5*U[1] - 10

# Print the Results
print("Solution of dU at Node 4 :", duEnd)
print("Solution of dU at Node 1 :", du0)

# Plot the Figure for the Solution of FEA
plt.figure()
plt.xlabel("Node Index")
plt.ylabel("Temperature in the Elements")
plt.title("Solution to the System of Equations and Elements for FEA")
plt.plot(np.linspace(1, 4, 4), U)
plt.show()