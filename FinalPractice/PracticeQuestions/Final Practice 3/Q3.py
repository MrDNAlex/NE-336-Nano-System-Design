from scipy.integrate import solve_ivp, solve_bvp
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt



T0 = 120
Q = 1000
k = 14

n = 6
x0 = 0.05
xEnd = 0.1
xVals = np.linspace(x0, xEnd, n)
dx = xVals[1] - xVals[0]

internalNodes = n - 1



# Make A Matrix
Amid = np.ones(internalNodes) * -2

Aup = np.ones(internalNodes-1) * (1 + dx/(2*xVals[1:-1]))

Adown = np.ones(internalNodes-1) * (1 - dx/(2*xVals[2:]))

A = np.diag(Amid) + np.diag(Aup, 1) + np.diag(Adown, -1)

A[-1, :] = 0
A[-1, -1] = 3
A[-1, -2] = -4
A[-1, -3] = 1

print(A)

b = np.zeros(internalNodes)

b[0] = -T0*(1-dx/(2*xVals[1]))
b[-1] = - (dx*Q)/(np.pi * k * xEnd)

solution = np.linalg.solve(A, b)

T = np.zeros(n)

T[0] = T0

T[1:] = solution

print(T)

dT = np.zeros(n)

dT[0] = (-T[2] + 4*T[1] - 3*T[0])/(2*dx)

dT [1:-1] = (T[2:] - T[:-2])/(2*dx)

dT[-1] = (3*T[-1] - 4*T[-2] + T[-3])/(2*dx)

fig, ax1 = plt.subplots()

ax1.plot(xVals, T)

ax2 = ax1.twinx()

ax2.plot(xVals, dT)
plt.show()