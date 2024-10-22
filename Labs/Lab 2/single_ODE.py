#Imports
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# ODE Function
def ode_fun_1 (t, x):
    beta = 2
    return beta * x * np.sin(beta * t)

# Define values for the Problem (Init Condition, Number of Points, Initial T, Final T)
InitialCondition = 5
tInit = 10
tFinal = 20

#Get the Solution of the ODE
sol1 = solve_ivp(ode_fun_1, [tInit, tFinal], [InitialCondition], method="RK45")

# Extract the Y and T Data
xVals = sol1.y[0]
tVals = sol1.t

# Plot the Solution for Q1
plt.figure()
plt.title("Solution to the ODE Using Solve_IVP (Q1)")
plt.plot(tVals, xVals, "r-", label=f"Solution using No T Span")
plt.legend()
plt.xlabel('Time')
plt.ylabel('x')
plt.show()

#
# Q2
# 

# Get the Value at T = 15
# We know that T = 15 is at the center of the Graph, or if we use the

# Add n to indentify number of points in t span
n = 100

# Generate T span
t_span = np.linspace(tInit, tFinal, n)

#Get the Solution of the ODE
sol1 = solve_ivp(ode_fun_1, [tInit, tFinal], [InitialCondition], method="RK45", t_eval=t_span)

# Extract the Y Data
xVals = sol1.y[0]

# Plot the Solution
plt.figure()
plt.title("Solution to the ODE Using Solve_IVP (Q2)")
plt.plot(t_span, xVals, "r-", label=f"Solution using T Span with n = {n} points")
plt.legend()
plt.xlabel('Time')
plt.ylabel('x')
plt.show()

# Print the value at T = 15 (Which is at index n/2)
print("\n")
print(f"(Q2) Solution at t=15 is : {xVals[int(n/2)]}")
print("\n")

#
# Q3
#

# Define the New Function
def ode_fun_2 (t, x, Beta):
    return Beta * x * np.sin(Beta * t)

# Add n to indentify number of points in t span
n = 100

# Define Beta Value to input as Argument in new Function
Beta = 2

# Generate T span
t_span = np.linspace(tInit, tFinal, n)

#Get the Solution of the ODE
sol1 = solve_ivp(ode_fun_2, [tInit, tFinal], [InitialCondition], method="RK45", t_eval=t_span, args=(Beta, ))

# Extract the Y Data
xVals = sol1.y[0]

# Plot the Solution
plt.figure()
plt.title("Solution to the ODE Using Solve_IVP (Q3)")
plt.plot(t_span, xVals, "r-", label=f"Solution using Args=(Beta)")
plt.legend()
plt.xlabel('Time')
plt.ylabel('x')
plt.show()

#
# Q4 and 5
#

# Add n to indentify number of points in t span (Increased n for Funsies)
n = 300

# Define Beta Value to input as Argument in new Function
Betas = [2, 4, 6, 8]

# Define Colors for Plotting
Colors = ["r-", "b-", "g-", "m-"]

# Generate T span
t_span = np.linspace(tInit, tFinal, n)

# Start Defining the Plotting Data
# Plot the Solution
plt.figure()
plt.title("Solutions to the ODE Using Solve_IVP with Multiple Betas (Q4 and Q5)")
plt.xlabel('Time')
plt.ylabel('x')

# Loop through all betas
for i in range(len(Betas)):
    #Get the Solution of the ODE
    sol1 = solve_ivp(ode_fun_2, [tInit, tFinal], [InitialCondition], method="RK45", t_eval=t_span, args=(Betas[i], ))

    # Extract the Y Data
    xVals = sol1.y[0]
    
    #Plot the individual Solution
    plt.plot(t_span, xVals, Colors[i], label=f"Solution Beta = {Betas[i]}")

# Show the Plot
plt.legend()
plt.show()