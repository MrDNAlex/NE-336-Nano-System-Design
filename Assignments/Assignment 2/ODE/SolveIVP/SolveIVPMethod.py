import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#
# Solve_IVP Method
#

# Create Lambda function for the function 
dydt = lambda t,y: (1+4*t)*np.sqrt(y)

# Create Lambda function for the Analytical Solution for Comparison
realSol = lambda t: ((t + 2*t**2+2)/2)**2 

# Initialize Key Values (Boundaries and Step Size)
(t0,tend)=(0,1)
h = 0.25

# Get Number of Points
n = int((tend - t0)/h) + 1

# Get T value Ranges
t = np.linspace(t0, tend, n)
tReal = np.linspace(t0, tend, 50)

# Get the True Solution
yValsReal = realSol(tReal)

# Initial Boundary Condition
y0 = 1

# Solve the ODE
result = solve_ivp(dydt, [t0, tend], [y0], t_eval=t)

# Get the Solution
yVals = result.y[0]

# Print Values
print("\n")
print(f"T Values (IVP) : {t}")
print(f"Solve_IVP Method : {yVals}")
print(f"True Solution : {realSol(t)}")
print("\n")

# Plot Eulers Method Vs the True Solution
plt.figure()
plt.title("Solution to the ODE : Solve_IVP")
plt.plot(t,yVals,'k-',label=f'Solve_IVP with dt={h}')
plt.plot(tReal,yValsReal,'r:',label='real')
plt.legend()
plt.xlabel('time')
plt.ylabel('y')
plt.show()
