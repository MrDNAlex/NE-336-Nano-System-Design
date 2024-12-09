from scipy.integrate import solve_ivp, solve_bvp
from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

n = 1000
D = 1.2 * 10**(-9)
k = 0.001
Ca0 = 0.2
x0 = 0
xEnd = 0.001

xVals = np.linspace(x0, xEnd, n)



def dfdx (x, f):
    
    [Ca, u] = f
    
    du = (k*Ca)/D
    
    return [u, du]


def BCs (fa, fb):
    
    BC1 = fa[0] - Ca0
    
    BC2 = fb[1]
    
    return [BC1, BC2]

CaInit = np.zeros((2, xVals.size))

solution = solve_bvp(dfdx, BCs, xVals, CaInit)





#
# Solve IVP Method
#


def Solver (uGuess):
    
    yGuess = solve_ivp(dfdx, (x0, xEnd), [Ca0, uGuess[0]])
    
    return yGuess.y[1, -1]

uGuess = [-10]

uCorrect = fsolve(Solver, uGuess)

sol = solve_ivp(dfdx, (x0, xEnd), [Ca0, uCorrect[0]], t_eval=xVals)

CaSol = sol.y[0]
dCa = sol.y[1]

fig, ax1 = plt.subplots()

ax1.plot(xVals, solution.y[0], "-", label="BVP")
ax1.plot(xVals, CaSol, "r--", label="IVP")
ax1.legend()


ax2 = ax1.twinx()
ax2.plot(xVals, solution.y[1], "-", label="BVP")
ax2.plot(xVals, dCa, "r--", label="IVP")
ax2.legend()

plt.show()
