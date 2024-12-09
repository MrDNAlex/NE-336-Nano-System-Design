from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define values
k = 35
D = 1.5 *10**(-9) * (10**(6))**2
C0 = 0.03
CEnd = 0

x0 = 0
xEnd = 50
dx = 1
n = int((xEnd - x0)/dx + 1)
xVals = np.linspace(x0, xEnd, n)

dt = 0.01
t0 = 0
tEnd = 0.1
nt = int((tEnd - t0) / dt + 1)

tVals = np.linspace(t0, tEnd, nt)

CInit = np.zeros(n-1)

def Matrix (x, C):
    
    Call = np.hstack([C0, C])
    
    dC = np.zeros(C.size)
    
    Ddx2 = D/dx**2
    
    dC[-1] = 2*Ddx2*(Call[-2] - Call[-1]) - k*Call[-1]
    
    dC[0:-1] = D*(Call[2:] - 2*Call[1:-1] + Call[:-2])/(dx**2) - k*Call[1:-1]
    
    return dC

solution = solve_ivp(Matrix, (t0, tEnd), CInit, t_eval=tVals)

CSol = np.vstack([np.ones(solution.t.size) * C0, solution.y])

print(CSol)

plt.figure(figsize=(16, 10))

for i in range(nt):
    plt.plot(xVals, CSol[:, i], label=f"t={i*0.01}")
plt.legend()
plt.show()