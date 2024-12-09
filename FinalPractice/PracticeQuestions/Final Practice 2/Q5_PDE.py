from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define values
x0 = 0
xEnd = 50 # Micrometer
dx = 0.5
n = int((xEnd - x0)/dx + 1)

# Define the Variables
C0 = 0.03
k = 35
D = 1.5 * 10**(-9) * (10**6)**2 # m^2/s * (10**6 um)^2 / 1 m^2 (Make a Unit Change)

lam = D/dx**2

xVals = np.linspace(x0, xEnd, n)

t0 = 0
tEnd = 0.1
dt = 0.01
tNodes = int((tEnd - t0)/dt + 1)
tVals = np.linspace(t0, tEnd, tNodes)

def dCdt (t, C):
    
    Call = np.hstack([C0, C])
    
    dC = np.zeros(C.size)
    
    dC[-1] = lam*(-2*Call[-1] + 2*Call[-2]) - k*Call[-1]
    
    dC[0:-1] = lam*(Call[2:] - 2*Call[1:-1] + Call[:-2]) - k*Call[1:-1]
    
    return dC

Cinit = np.zeros(n-1)

solution = solve_ivp(dCdt, (t0, tEnd), Cinit, t_eval=tVals)

Csol = np.vstack([np.ones(tNodes) * C0, solution.y])



plt.figure()
for i in range(tNodes):
    plt.cla()
    plt.plot(xVals, Csol[:,i])
    plt.pause(0.1)
    
plt.show()
