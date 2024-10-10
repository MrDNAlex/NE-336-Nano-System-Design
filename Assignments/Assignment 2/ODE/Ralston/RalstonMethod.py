import numpy as np
import matplotlib.pyplot as plt

#
# Ralston Method
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

# Initialize Y Values Array, Apply Initial Boundary Condition
yVals = np.zeros(n)
yVals[0] = y0

# Ralston / RK2 Method Properties
a1 =1/4
a2 = 3/4
p1 = 2/3

# Loop over all Values and calculate new Index
for i in range(1, n):
    # Calculate K1
    k1 = dydt(yVals[i-1], t[i-1])
    
    # Calculate Inputs for K2 and K2 itself
    yk2 = yVals[i-1]+p1*k1*h
    tk2 = t[i-1]+p1*h
    k2 = dydt(yk2, tk2)
    
    # Update Y Val
    yVals[i] = yVals[i-1] + (a1*k1 + a2*k2)*h

# Print Values
print("\n")
print(f"T Values : {t}")
print(f"Ralston Method : {yVals}")
print(f"True Solution : {realSol(t)}")
print("\n")

# Plot Eulers Method Vs the True Solution
plt.figure()
plt.title("Solution to the ODE : Ralston")
plt.plot(t,yVals,'k-',label=f'Ralston with dt={h}')
plt.plot(tReal,yValsReal,'r:',label='real')
plt.legend()
plt.xlabel('time')
plt.ylabel('y')
plt.show()