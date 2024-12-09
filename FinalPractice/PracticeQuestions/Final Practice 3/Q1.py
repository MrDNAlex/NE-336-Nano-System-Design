from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


M0 = 1000
S0 = 200

n = 1000
t0 = 0
tEnd = 120
tVals = np.linspace(t0, tEnd, n)

def dfdt (t, f):
    [M, S] = f
    
    EQ1 = 10
    
    EQ2 = 10*0.2 - 10 *(S/M)
    
    return [EQ1,  EQ2]

init = [M0, S0]

solution = solve_ivp(dfdt, (t0, tEnd), init, t_eval=tVals)

Msol = solution.y[0]
Ssol = solution.y[1] 


fig , ax1 = plt.subplots()

ax1.plot(tVals, Msol,"b-", label="M")
ax1.legend()

ax2 = ax1.twinx()

ax2.plot(tVals, Ssol, "r--", label="S")
ax2.legend()

plt.show()

plt.figure()
plt.plot(tVals, Ssol/Msol, label="S/M")
plt.legend()
plt.show()

