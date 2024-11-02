import numpy as np
from scipy.integrate import solve_ivp, solve_bvp
import matplotlib.pyplot as plt

# Constants
L = 1.0  # cm, length of the cylindrical pore
CA0 = 1.0e-3  # mol/cm^3, initial concentration at x = 0
k = 10.0  # cm^3/mol s, reaction rate constant
DA = 1.0e-3  # cm^2/s, diffusion coefficient

# Define the system of ODEs
def odes(x, y):
    return [y[1], (k * y[0]**2)/DA]

# Boundary condition for solve_bvp
def bc(ya, yb):
    return [ya[0] - CA0, yb[1]]

# Initial mesh
x = np.linspace(0, L, 50)

# Initial guess for the solution
y_guess = np.zeros((2, x.size))
y_guess[0] = np.linspace(CA0, CA0/2, x.size)  # Linear interpolation as a guess

# Solve with solve_bvp
sol_bvp = solve_bvp(odes, bc, x, y_guess)

# Shooting method using solve_ivp
def shoot(dy0):
    sol = solve_ivp(odes, [0, L], [CA0, dy0], t_eval=np.linspace(0, L, 100))
    return sol.y[1, -1]

from scipy.optimize import newton
dy0_guess = -0.001  # Initial guess for the derivative at x=0
dy0_solution = newton(shoot, dy0_guess)
sol_ivp = solve_ivp(odes, [0, L], [CA0, dy0_solution], t_eval=np.linspace(0, L, 100))

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(sol_bvp.x, sol_bvp.y[0], label='solve_bvp', linestyle='-', marker='o')
plt.plot(sol_ivp.t, sol_ivp.y[0], label='solve_ivp (shooting)', linestyle='--')
plt.xlabel('Position, x (cm)')
plt.ylabel('Concentration, $C_A$ (mol/cm$^3$)')
plt.title('Concentration Profile of Species A in a Cylindrical Pore')
plt.legend()
plt.grid(True)
plt.show()

# Save to a file
plt.savefig('system_ODEs_question2_plot.png')
