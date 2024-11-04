#Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Time Import
import time

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Define the System of Equations
def GEARsystem (t, y):
    [x1, x2, x3] = y
    
    dx1dt = -0.013*x1 - 1000*x1*x3
    dx2dt = -2500*x2*x3
    dx3dt = -0.013*x1 - 1000*x1*x3 - 2500*x2*x3
    
    return [dx1dt, dx2dt, dx3dt]

# Define the Initial Conditions of the Problem
initialConditions = [1, 1, 0]

# Define all the Methods to test, First 3 are Explicit, last 3 Implicit
IVPMethods = ["RK45", "RK23", "DOP853", "Radau", "BDF", "LSODA" ]

# Define 10 Iterations to Run through So that we can get a average time of each method as it fluctuates
iterationNums = 10

# Have a Dictionary to Store each Iteration
iterations = {}

# Loop through a Number of Iterations
for i in range(iterationNums):

    # Create a Empty Dictionary for the Results
    results = {}

    # Print a Gap cause my Terminal acts Weird
    print("\n")
    print(f"Iteration {i}")

    # Loop through Every IVP Method
    for method in IVPMethods:
        
        # Record the Start Time
        startTime = time.time()
        
        # Run the Solver
        sol = solve_ivp(GEARsystem, (0, 50), initialConditions, method=method)

        # Record the End Time
        endTime = time.time()
        
        # Calculate Delta t in Seconds
        deltaTime = endTime - startTime 
        
        # Store the results in the Dictionary
        results[method] = deltaTime
        
        # Print the Results for the Method
        print(f"Method : {method} Elapsed Time : {deltaTime} sec")
        
    iterations[i] = results
    
    
# Calculate the average times for each method
average_times = {method: 0 for method in IVPMethods}

# Add up all the times
for results in iterations.values():
    for method, time in results.items():
        average_times[method] += time

# Divide by the number of iterations to get the average
for method in average_times:
    average_times[method] /= iterationNums

# Print out the Final Results
print("\n")
print("Average Time of each Method")
for key in average_times.keys():
    print(f"Method : {key} Elapsed Time : {average_times[key]} sec")

# Make a Bar Graph displaying Time of each Solver Method
plt.figure(figsize=(10, 6))
plt.bar(average_times.keys(), average_times.values())
plt.xlabel("Solve Method")
plt.ylabel("Time Elapsed to Solve")
plt.title("Comparison of Solver Methods by Average Time Taken")
plt.savefig("SolveTime.png")
plt.show()