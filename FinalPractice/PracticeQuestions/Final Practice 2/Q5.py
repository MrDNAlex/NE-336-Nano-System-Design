from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define values
x0 = 0
xEnd = 50 # Micrometer
dx = 1
n = int((xEnd - x0)/dx + 1)

# Define the Variables
C0 = 0.03
k = 35
D = 1.5 * 10**(-9) * (10**6)**2 # m^2/s * (10**6 um)^2 / 1 m^2 (Make a Unit Change)

xVals = np.linspace(x0, xEnd, n)

CInit = np.zeros(n)

def dCdx (x, f):
    [C, u] = f
    
    du = k*C/D
    
    return [u, du]

def Solver (uGuess):
    
    yGuess = solve_ivp(dCdx, (x0, xEnd), [C0, uGuess[0]])
    
    return yGuess.y[1, -1]

uGuess = [-10]

uCorrect = fsolve(Solver, uGuess)

solution = solve_ivp(dCdx, (x0, xEnd), [C0, uCorrect[0]], t_eval=xVals)

CSol = solution.y[0]

plt.figure()
plt.plot(xVals, CSol)
plt.plot(xVals, solution.y[1])
plt.show()