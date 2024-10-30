# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:50:52 2024

@author: a3dufres
"""
# Imports
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define the function
def dydt (t, y):
    
    return 5*(y - t**2)

# Initial Conditions
# y(t=0) = 0.08
y0 = [0.08]


# Define the Start and End
(t0, tend) = (0, 2)

# Define a list of all the RK Methods (First 3 are Explicit, last one is Implicit)
RKMethods = ["RK45", "RK23", "DOP853", "Radau" ]

plt.figure()
# Solve for multiple Runge Kutta Methods
for rk in RKMethods:
    sol = solve_ivp(dydt, [t0, tend],y0, method=rk)
    plt.plot(sol.t, sol.y[0], label=f"RK Method = {rk}")
    
plt.legend()
plt.title("Solution to the Q1 ODE")
plt.xlabel("Time (t)")
plt.ylabel("Value of Y (y)")
plt.show()

# Q1 b
# The least accurate method appears to be the RK23 method, it is quite odd that it does not converge properly
# If we exclude that method since it is obviously wrong, the next worst method is the Radau method

# Bonus 1
# The reason the methods disagree is due to the order of the different methods, Higher order methods such as dop853, require more calculations and yield better results. Lower order methods will sample less points and will be less accurate but quicker to run

# !!! PS May need to comment out this code to look at the first graph !!!
# Bonus 2
# To force them all to agree we will define the number of points to calculate for and make it a large number so that deviations are small (Smaller delat T gives better results)
# Define number of Points
n = 1000

# Linspace for all of t
tSpan = np.linspace(t0, tend, n)

plt.figure()
# Solve for multiple Runge Kutta Methods
for rk in RKMethods:
    sol = solve_ivp(dydt, [t0, tend],y0, method=rk, t_eval=tSpan)
    plt.plot(sol.t, sol.y[0], label=f"RK Method = {rk}")
    
plt.legend()
plt.title("Solution to the Q1 ODE")
plt.xlabel("Time (t)")
plt.ylabel("Value of Y (y)")
plt.show()