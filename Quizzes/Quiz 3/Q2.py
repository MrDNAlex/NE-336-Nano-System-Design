# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:07:17 2024

@author: a3dufres
"""
# Imports
import numpy as np
import matplotlib.pyplot as plt

 
#
# Alexandre Dufresne-Nappert
# 20948586
#

# Number of Internal Nodes
n = 100

# Define the R Min and R Max
rMin = 5
rMax = 10

# Define the Start and End Temp
TInit = 20
TEnd = 200

# Define r Vector
r = np.linspace(rMin, rMax, n+2)

# Define dr
dr = (rMax - rMin)/(n + 1)

# Create the D and E Variable which are for the i+1 and i-1 on the diagonals
D = np.ones(n-1) * ((1/dr**2)+ 1/(2*r[1:-2]*dr))
E = np.ones(n-1) * ((1/dr**2)- 1/(2*r[2:-1]*dr))

# Define the A Matrix
A = np.diag(np.ones(n) * ((-2)/dr**2)) + np.diag(D, 1) + np.diag(E, -1)


# Define the b Vector
b = np.zeros(n)

# Apply the Boundary Values
b[0] = -TInit * (1/dr**2 - 1/(2*r[1]*dr))
b[-1] = -TEnd * (1/dr**2 + 1/(2*r[-2]*dr))

# Solve the Solution
sol = np.linalg.solve(A, b)

# Make the T Vector
T = np.zeros(n+2)

# Apply Initial and End Value
T[0] = TInit
T[-1] = TEnd

# Apply the Solution
T[1:-1] = sol

# Graph the Solution
plt.figure()
plt.plot(r, T, "--")
plt.xlabel("Radius (m)")
plt.ylabel("Temperature")
plt.title("Solution to the Radial Heat Distribution")
plt.show() 
