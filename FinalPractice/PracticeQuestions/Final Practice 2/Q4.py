from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define values
xEnd = 0.1
x0 = 0
n = 100

T0 = 100
h = 20
k = 14
Tair = 20

r = lambda x: 0.02 - 0.1*x

def dTdx (x, f):
    [T, u] = f
    
    du = (0.2*u + (2*h)/k * (T - Tair))/r(x)
    
    return [u, du]


def BCs (To, TL):
    
    BC1 = To[0] - T0
    BC2 = k*TL[1] + h*(TL[0] - Tair)
    
    return [BC1, BC2]

xVals = np.linspace(x0, xEnd, n)
TVals = np.zeros((2, xVals.size))

solution = solve_bvp(dTdx, BCs, xVals, TVals)

TSol = solution.y[0]

plt.figure()
plt.plot(xVals, TSol)
plt.plot(xVals, solution.y[1] * r(xVals) **2 )
plt.show()