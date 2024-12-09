from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define values
n = 100
k = 35
D = 1.5 *10**(-9) * (10**(6))**2
C0 = 0.03
CEnd = 0

x0 = 0
xEnd = 50 

def dCdx (x, f):
    [C, u] = f
    
    return [u, (k*C)/D]

xVals = np.linspace(x0, xEnd, n)
CVals = np.zeros((2, xVals.size))

def Solver (uGuess):
    
    yGuess = solve_ivp(dCdx, (x0, xEnd), [C0, uGuess[0]], t_eval=xVals)
    
    # Return Residual of 2 BCs
    return np.abs(yGuess.y[1, -1]) + np.abs(yGuess.y[0, -1])

uGuess = [-10]

uVal = fsolve(Solver, uGuess)

solution = solve_ivp(dCdx, (x0, xEnd), [C0, uVal[0]], t_eval=xVals)

CSol = solution.y[0]

print(CSol)

plt.figure(figsize=(16, 10))
plt.plot(xVals, CSol)
plt.plot(xVals, solution.y[1])
plt.show()