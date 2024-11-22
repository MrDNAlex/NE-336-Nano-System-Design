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

# Define lambda
lam = 1 / (2 * dr**2)

# Initial condition: u(r, 0) = 0 for all r
UInit = np.zeros(n)

# Define the ODE system (dU/dz = f(U))
def dUdz(z, U):
    dU = np.zeros_like(U)
    
    # Boundary condition at r = 0 (Neumann, insulated boundary)
    dU[0] = 2 * lam * (U[1] - U[0])
    
    # Interior points
    for i in range(1, n - 1):
        ri = rVals[i]
        dU[i] = lam * (1 + dr / (2 * ri)) * U[i + 1] - 2 * lam * U[i] + lam * (1 - dr / (2 * ri)) * U[i - 1]
    
    # Boundary condition at r = 1 (Dirichlet, fixed value)
    dU[-1] = 0  # u(1, z) = 1 is directly enforced in the solver
    
    return dU

# Solve the ODE system with Dirichlet boundary enforced
def enforce_boundary_conditions(U):
    U[-1] = 1  # Dirichlet condition at r = 1
    return U

# Define a wrapper for solve_ivp to enforce boundary conditions
def ode_with_bc(z, U):
    U = enforce_boundary_conditions(U)
    return dUdz(z, U)

# Solve the system
solution = solve_ivp(ode_with_bc, (zInit, zEnd), UInit, t_eval=tVals, method="RK45")

# Apply boundary conditions to the solution
for i in range(solution.y.shape[1]):
    solution.y[:, i] = enforce_boundary_conditions(solution.y[:, i])

# Plot results
plt.figure(figsize=(8, 6))
for i in range(0, len(tVals), max(1, len(tVals) // 10)):  # Plot a few time steps
    plt.plot(rVals, solution.y[:, i], label=f"z={tVals[i]:.2f}")
plt.xlabel(r"$\bar{r}$")
plt.ylabel(r"$u(\bar{r}, \bar{z})$")
plt.title("Temperature Distribution Using MOL")
plt.legend()
plt.grid()
plt.show()
