from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define the Values
r1 = 0.05
r2 = 0.10
n = 6
Q = 1000
k = 14

TInit = 120

# Define the R vector
rVals = np.linspace(r1, r2, n)

ri = rVals[1:]

dr = (ri[1] - ri[0])


print("Dr : ", dr)

# Define the A Matrix (Split into 3 parts)
Amid = np.ones(n-1) * -2
Aup = np.ones(n - 2) * (1 + dr/(2*ri[:-1]))
Adown = np.ones(n - 2) * (1-dr/(2*ri[1:]))

# Combine the A Matrix
A = np.diag(Amid) + np.diag(Aup, 1) + np.diag(Adown, -1)

# Apply Backwards Difference at the end
A[-1, :] = 0
A[-1, -1] = 3
A[-1, -2] = -4
A[-1, -3] = 1

# Define the b vector
b = np.zeros(n-1)

# Apply Boundary Conditions
b[0] = -TInit*(1-dr/(2*rVals[1]))
b[-1] = -(dr*Q)/(np.pi*r2*k)

solution = np.linalg.solve(A, b)

# Create Matrix and Paste Solution
T = np.zeros(n)
T[0] = TInit
T[1:] = solution

fig, ax1 = plt.subplots()
#plt.figure(figsize=(16, 10))
ax1.plot(rVals, T, label="T")
ax1.legend()

# Get the Gradient
DT = np.zeros(n)

DT[0] = (-T[2] + 4*T[1] - 3*T[0])/(2*dr)

DT[1:-1] = (T[2:] - T[:-2])/(2*dr)

DT[-1] = (1/(2*dr)) * (3*T[-1] - 4*T[-2] + T[-3])

ax2 = ax1.twinx()
ax2.plot(rVals, DT, "--", label="dT")
ax2.legend()
plt.show()