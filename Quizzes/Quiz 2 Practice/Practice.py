import numpy as np
from scipy.integrate import solve_ivp, solve_bvp
import matplotlib.pyplot as plt

# Solve IVP Method

# Define the Function
def dfdt (t, f, mew, A, w):
    # f = x, dxdt
    # dfdt = u, mew*(1-x**2)dxdt-x+Asin(wt)
    
    [x, u] = f
    
    return [u, mew*(1-x**2)*u-x+A*np.sin(w*t) ]

plt.figure()
# Loop through all Mu Values
for m in [0, 1, 2]:
    sol = solve_ivp(dfdt, (0, 25), [1, 1], args=(m, 0, 2))
    
    print(sol)
    # Plot X vs DxDt  (So DxDt on the x axis)
    plt.plot(sol.y[1], sol.y[0], label=f"mu = {m}")


plt.legend()
plt.show()

# Plot Question b
plt.figure()
for m in [0]:
    sol = solve_ivp(dfdt, (0, 25), [1, 1], args=(m, 0, 2))
    
    # Plot X vs DxDt  (So DxDt on the x axis)
    plt.plot(sol.t, sol.y[0], label=f"x (mu = {m})")
    plt.plot(sol.t, sol.y[1], label=f"dxdt (mu = {m})")


plt.legend()
plt.show()









#
# Shooting method
#

# Question 2 : Linear Function


# Solve BVP Method

# Define the function
def dfdx (x, f):
    [y, u] = f
    
    return [u, -x*u+10*y]

def BCs (fa, fb):
    
    # fa[0] is for boundary condition of y
    # fa[1] is for boundary condition of dydx
    
    return [fa[1] - 20, fb[1] - 10*fb[0] - 5]

tVals = np.linspace(0, 10, 1000)
yVals = np.zeros((2, tVals.size))

bvp_sol = solve_bvp(dfdx, BCs, tVals, yVals)

plt.close()
plt.figure()

plt.plot(tVals, bvp_sol.y[0])
plt.show()