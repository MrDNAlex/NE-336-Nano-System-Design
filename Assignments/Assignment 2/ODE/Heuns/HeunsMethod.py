import numpy as np
import matplotlib.pyplot as plt

#
# Heuns Method
#

# Create Lambda function for the function
dydt = lambda y,t: (1+4*t)*np.sqrt(y)

# Create Lambda function for the Analytical Solution for Comparison
realSol = lambda t: ((t + 2*t**2+2)/2)**2 

# Initialize Key Values (T Boundaries, Step Size and Initial Boundary Conditions)
(t0,tend)=(0,1)
h = 0.25
y0 = 1

# Get Number of Points
n = int((tend - t0)/h) + 1

# Get T value Ranges
t = np.linspace(t0, tend, n)
tReal = np.linspace(t0, tend, 50)

# Get the True Solution
yValsReal = realSol(tReal)

# Initialize Y Values Array, Apply Initial Boundary Condition
yVals = np.zeros(n)
yVals[0] = y0

# Loop over all Values and calculate new Index
for i in range(1, n):
    
    # Take one iteration of Euler Method
    yStar = yVals[i-1] + dydt(yVals[i-1], t[i-1])*h
    
    # Under normal conditions we would loop this equation to update yStar until we reach a tolerance
    # Then we can update yVals[i]. But since we are told not to iterate we can simplfy to a single Equation
    yVals[i] = yVals[i-1] + 0.5*(dydt(yVals[i-1], t[i-1]) + dydt(yStar, t[i-1]))*h

# Print Values
print("\n")
print(f"T Values : {t}")
print(f"Heuns Method : {yVals}")
print(f"True Solution : {realSol(t)}")
print("\n")

# Plot Eulers Method Vs the True Solution
plt.figure()
plt.title("Solution to the ODE : Heuns")
plt.plot(t,yVals,'k-',label=f'heuns with dt={h}')
plt.plot(tReal,yValsReal,'r:',label='real')
plt.legend()
plt.xlabel('time')
plt.ylabel('y')
plt.show()