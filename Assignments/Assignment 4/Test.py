import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define parameters
dr = 0.2  # Spatial step size
rInit, rEnd = 0, 1
rNodes = int((rEnd - rInit) / dr + 1)
rVals = np.linspace(rInit, rEnd, rNodes)

dt = 0.01  # Time step size
zInit, zEnd = 0, 1.0
tVals = np.arange(zInit, zEnd + dt, dt)

# Number of spatial points
n = len(rVals)

# Define the lambda (for MOL spatial discretization)
lam = 1 / (2 * dr**2)

# Boundary values
URight = 1  # u(1, z) = 1
UInit = np.zeros(n)  # u(r, 0) = 0

# Define the ODE system (dU/dz = f(U))
def dUdz(z, U):
    dU = np.zeros_like(U)  # Initialize derivative array
    
    # Boundary conditions
    dU[0] = 2 * lam * (U[1] - U[0])  # Neumann boundary at r=0
    dU[-1] = 0  # Dirichlet boundary at r=1 (constant u = 1)
    
    # Interior points
    for i in range(1, n - 1):
        ri = rVals[i]
        dU[i] = lam * (1 + dr / (2 * ri)) * U[i + 1] - 2 * lam * U[i] + lam * (1 - dr / (2 * ri)) * U[i - 1]
    
    return dU

# Solve the ODE system
solution = solve_ivp(dUdz, (zInit, zEnd), UInit, t_eval=tVals, method="RK45")

# Extract solution
uVals = solution.y

# Plot results
plt.figure(figsize=(8, 6))
for i in range(0, len(tVals), max(1, len(tVals) // 10)):  # Plot a few time steps
    plt.plot(rVals, uVals[:, i], label=f"z={tVals[i]:.2f}")
plt.xlabel(r"$\bar{r}$")
plt.ylabel(r"$u(\bar{r}, \bar{z})$")
plt.title("Temperature Distribution Using MOL")
plt.legend()
plt.grid()
plt.show()
