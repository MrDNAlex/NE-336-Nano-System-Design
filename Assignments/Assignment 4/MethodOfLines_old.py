# Imports
import numpy as np
from scipy.integrate import solve_bvp, solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# Number of Internal Nodes (4 + 1 (Derivative BC))
n = 4

# Define the Right Boundary
URight = 1
UInit = 0

# Define dr the Start, End and Number of Space Nodes, and create the array of Values
dr = 0.2
rInit = 0
rEnd = 1
rNodes = int((rEnd - rInit)/dr + 1)
rVals = np.linspace(rInit, rEnd, rNodes)

# Define Lambda
lam = 1/(2*dr**2)

#Using t instead of z
# Define dt the Start, End and Number of Time Nodes, and create the array of Values
dt = 0.01 
tInit = 0
tEnd = 1.0
tNodes = int((tEnd - tInit)/dt + 1)
tVals = np.linspace(tInit, tEnd, tNodes)

## Define the dU/dt Function
def dUdt (t, U):
    
    FullU = np.hstack([U, URight])
    
    print(FullU)
    
    dU = np.zeros(U.size)
    
    print("Hello", len(dU))
    
    dU[0] = 2*lam*FullU[1] - 2*lam*FullU[0]
    
    for i in range(1, n ):
        
        print(i)
        
        ri = rVals[i]
        
        dU[i] = lam*(1 + dr/(2 * ri)) * FullU[i + 1] - 2*lam*FullU[i] + lam*(1 - dr/(2 * ri)) * FullU[i - 1]
            
    dU[-1] = -2*lam*FullU[-2] + lam*(1 - dr/(2 * rVals[-2])) * FullU[-3] + lam*(1 + dr/(2*rVals[-2]))        
    
    return dU
        


#solution = solve_ivp(dUdt, (0, 1), np.zeros(n+1), t_eval=tVals)
#
#
#for i in range(len(solution.y)):
#    print(solution.y[i])
#
#
#
#
#print(len(solution.y[0]))
#
#print(solution)
#
#tVals = solution.t
#sol = np.vstack([solution.y, URight*np.ones(n)])
#
#print(sol)
#
#plt.figure()
#plt.plot(tVals, )

# Define the dU/dt Function
#def dUdt(t, U):
#    FullU = np.hstack([U, URight])  # Add boundary condition to the right
#    
#    dU = np.zeros(U.size)  # Initialize derivative array
#    
#    # Boundary conditions
#    dU[0] = 2 * lam * FullU[1] - 2 * lam * FullU[0]  # Left boundary
#    dU[-1] = -2 * lam * FullU[-2] + lam * (1 - dr / (2 * rVals[-2]))  # Right boundary
#    
#    # Interior nodes
#    for i in range(1, n - 1):
#        ri = rVals[i]
#        dU[i] = lam * (1 + dr / (2 * ri)) * FullU[i + 1] - 2 * lam * FullU[i] + lam * (1 - dr / (2 * ri)) * FullU[i - 1]
#    
#    return dU

# Solve the PDE
initial_condition = np.zeros(n+1)  # Initial condition for U
solution = solve_ivp(dUdt, (tInit, tEnd), initial_condition, t_eval=tVals)

print(solution.y)

# Extract and plot the solution
plt.figure()

idk = []


for i in range(n+1):
    
    plt.plot(tVals, solution.y[i], label=f'Node {i}')
plt.xlabel('Time')
plt.ylabel('U')
plt.legend()
plt.title('Evolution of U over Time')
plt.show()








