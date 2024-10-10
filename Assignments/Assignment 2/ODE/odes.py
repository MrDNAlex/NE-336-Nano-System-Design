import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#
# Setup
#

# Create Lambda function for the function
dydt = lambda y,t: (1+4*t)*np.sqrt(y)

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

#
# Eulers Method
#

# Initialize Y Values Array, Apply Initial Boundary Condition
yValsEuler = np.zeros(n)
yValsEuler[0] = y0

# Loop over all Values and calculate new Index
for i in range(1, n):
    yValsEuler[i] = yValsEuler[i-1] + dydt(yValsEuler[i-1], t[i-1])*h

#
# Heuns Method
#

# Initialize Y Values Array, Apply Initial Boundary Condition
yValsHeuns = np.zeros(n)
yValsHeuns[0] = y0

# Loop over all Values and calculate new Index
for i in range(1, n):
    
    # Take one iteration of Euler Method
    yStar = yValsHeuns[i-1] + dydt(yValsHeuns[i-1], t[i-1])*h
    
    # Under normal conditions we would loop this equation to update yStar until we reach a tolerance
    # Then we can update yVals[i]. But since we are told not to iterate we can simplfy to a single Equation
    yValsHeuns[i] = yValsHeuns[i-1] + 0.5*(dydt(yValsHeuns[i-1], t[i-1]) + dydt(yStar, t[i-1]))*h


#
# Ralston Method
#

# Initialize Y Values Array, Apply Initial Boundary Condition
yValsRalston = np.zeros(n)
yValsRalston[0] = y0

# Ralston / RK2 Method Properties
a1 =1/4
a2 = 3/4
p1 = 2/3

# Loop over all Values and calculate new Index
for i in range(1, n):
    # Calculate K1
    k1 = dydt(yValsRalston[i-1], t[i-1])
    
    # Calculate Inputs for K2 and K2 itself
    yk2 = yValsRalston[i-1]+p1*k1*h
    tk2 = t[i-1]+p1*h
    k2 = dydt(yk2, tk2)
    
    # Update Y Val
    yValsRalston[i] = yValsRalston[i-1] + (a1*k1 + a2*k2)*h


#
# Runge Kutta Method
#

# Initialize Y Values Array, Apply Initial Boundary Condition
yValsRK = np.zeros(n)
yValsRK[0] = y0

# Loop over all Values and calculate new Index
for i in range(1, n):
    # Calculate the K Values
    k1 = dydt(yValsRK[i-1], t[i-1])
    k2 = dydt(yValsRK[i-1] + 0.5*k1*h, t[i-1]+0.5*h)
    k3 = dydt(yValsRK[i-1] + 0.5*k2*h, t[i-1]+0.5*h)
    k4 = dydt(yValsRK[i-1]+k3*h, t[i-1]+h)
    
    # Calculate Phi
    phi = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    # Update Y Val
    yValsRK[i] = yValsRK[i-1] + phi*h

#
# Solve_IVP Method
#

# Create Lambda function for the function (Flipped)
dydt = lambda t,y: (1+4*t)*np.sqrt(y)

# Solve the ODE
result = solve_ivp(dydt, [0, 1], [1], t_eval=t)

# Get the Solution
yValsIVP = result.y[0]

#
# Printing Values and Graphing
#

# Print Values
print("\n")
print(f"T Values : {t}")
print(f"Euler Method : {yValsEuler}")
print(f"Heuns Method : {yValsHeuns}")
print(f"Ralston Method : {yValsRalston}") 
print(f"Runge-Kutta Method : {yValsRK}")
print(f"Solve_IVP Method : {yValsIVP}")
print(f"True Solution : {realSol(t)}")
print("\n")

# Plot Eulers Method Vs the True Solution
plt.figure()
plt.title("Solution to the ODE : All Methods")
plt.plot(tReal,yValsReal,'r-',label='real')
plt.plot(t,yValsEuler,'k*',label=f'euler with dt={h}')
plt.plot(t,yValsHeuns,'bs',label=f'heuns with dt={h}')
plt.plot(t,yValsRalston,'yv',label=f'Ralston with dt={h}')
plt.plot(t,yValsRK,'mo',label=f'Runge-Kutta with dt={h}')
plt.plot(t,yValsIVP,'g.',label=f'Solve_IVP with dt={h}')
plt.legend()
plt.xlabel('time')
plt.ylabel('y')
plt.show()
