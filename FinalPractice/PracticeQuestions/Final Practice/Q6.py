from scipy.integrate import solve_bvp, solve_ivp
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# Define values
alpha = 0.081

x0 = 0
xEnd = 20
dx = 2
xNodes = int((xEnd - x0)/dx + 1)
n = xNodes - 1
xVals = np.linspace(x0, xEnd, xNodes)

t0 = 0
tEnd = 1460
dt = 1
tNodes = int((tEnd - t0)/dt + 1)
tVals = np.linspace(t0, tEnd, tNodes)

lam = alpha/dx**2

T0 = lambda t: 10 - 14*np.cos(2*np.pi/365 * (t - 37))

def dTdt (t, T):
    
    TAll = np.hstack([T0(t), T])
    
    dT = np.zeros(n)
    
    dT[-1] = 2*TAll[-2] - 2*TAll[-1]
    
    dT[0:-1] = TAll[2:] -2*TAll[1:-1] + TAll[:-2]
    
    return dT * lam
    

TInit = np.ones(n) * 10

solution = solve_ivp(dTdt, (t0, tEnd), TInit, t_eval=tVals)

TSol = np.vstack([np.ones(tNodes) * T0(tVals), solution.y])

plt.figure()
for i in range(tNodes):
    plt.plot(xVals, TSol[:, i])
    
plt.show()
    
plt.figure()
for i in range(0,solution.t.size):
	plt.cla()
	plt.ylim([-5,20])
	plt.xlim([0,20])
	plt.plot(xVals,TSol[:,i])
	plt.title('Temperature profile at t = '+str(int(solution.t[i]))+'days')
	plt.xlabel('Depth [m]')
	plt.ylabel('T [degC]')
	plt.pause(0.01)
plt.show()
    