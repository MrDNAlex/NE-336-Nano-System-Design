#Imports
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define values for Problem
tFinal = 21
tInit = 0
n = 500
P0 = 0
L0 = 0
Z0 = 0

# Define t Span
tVals = np.linspace(tInit, tFinal, n)

def dxdt (t, x):
    #Unpack the Values
    L = x[0]
    P = x[1]
    Z = x[2]
    
    return [-3.6*L + 1.2*(P*(1-P**2) - 1),
            -1.2*P + 6 * (L + 2/(1+Z)),
            -0.12*Z + 12*P]
    
#Solve the System
sol = solve_ivp(dxdt, [tInit, tFinal], [P0, L0, Z0], method="RK45", t_eval=tVals)

# Extract X Datas
SolL = sol.y[0]
SolP = sol.y[1]
SolZ = sol.y[2]

# Create a Figure with 3 Plots
fig, axes = plt.subplots(1, 3)

# Subplot 1
axes[0].plot(tVals, SolL, "r-", label=f"Laura's love")
axes[0].plot(tVals, SolP, "b-", label=f"Petrarch's Love")
axes[0].plot(tVals, SolZ, "g-", label=f"Petrarch Inspiration")
axes[0].set_xlabel("Years")
axes[0].set_ylabel("Magnitudes of Esmotions")
axes[0].legend()

# Sublot 2
axes[1].plot(SolZ, SolP, "b-", label=f"P vs Z")
axes[1].set_xlabel("Petrarch Inspiration")
axes[1].set_ylabel("Petrarch's Love")
axes[1].legend()

# Subplot 3
axes[2].plot(SolP, SolL, "b-", label=f"L vs P")
axes[2].set_xlabel("Petrarch's Love")
axes[2].set_ylabel("Laura's Love")
axes[2].legend()

# Print the answer to the Bonus Question
print("\n")
print("Laura never did come to Love Petrarch over the 21 years, this is because Laura's love is always in the negatives and additionally in the first paragraph it is explained that Laura is a married woman, therefor she is not inclined to love another man")

# Show All 3 Plots
plt.suptitle("Solution to the System of ODE's of Petrarch's love of Laura")
plt.show()

