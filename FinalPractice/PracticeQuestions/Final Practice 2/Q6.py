from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define values
x0 = 0
xEnd = 20 # meter
dx = 2
xNodes = int((xEnd - x0)/dx + 1)
xVals = np.linspace(x0, xEnd, xNodes)

t0 = 0
tEnd = 1460
dt = 3
tNodes = int((tEnd - t0)/dt + 1)
tVals = np.linspace(t0, tEnd, tNodes)


alpha = 0.081

T0 = lambda t: 10 - 14 * np.cos(2*np.pi / 365 * (t - 37))

lam = alpha/dx**2

def dTdx (t, T):
    TAll = np.hstack([T0(t), T])
    
    dT = np.zeros(T.size)
    
    dT[-1] = (-2*TAll[-1] + 2*TAll[-2])
    
    dT[0:-1] = (TAll[2:] - 2* TAll[1:-1] + TAll[:-2])
    
    return lam*dT

TInit = np.ones(xNodes - 1) * 10

solution = solve_ivp(dTdx, (t0, tEnd), TInit, t_eval=tVals)

Tsol = np.vstack([np.ones(tNodes) * T0(tVals), solution.y])

plt.figure()
for i in range(tNodes):
    plt.cla()
    plt.ylim((-5, 20))
    plt.title("Temperature in the Ground over the Year")
    plt.xlabel("Distance in the soil (m)")
    plt.ylabel("Temperature of the Soil (Celsius)")
    plt.plot(xVals, Tsol[:, i])
    plt.pause(0.01)
plt.show()


# We must solve for more than one year because we are not told where the T0 function stops, so we need to repeat a few times. 
# Additionally depending on the depth of the dirt, there is lag on where the system would be


