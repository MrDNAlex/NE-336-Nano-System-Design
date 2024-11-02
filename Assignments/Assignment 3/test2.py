import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Constants
Ca0 = 1.0e-3  # mol/cm^3, initial concentration
xInit, xEnd = 0, 1.0  # Start and end positions in cm
k = 10.0  # cm^3/mol s, reaction rate constant

# Define the system of ODEs
def dfdx(x, y):
    Ca, u = y
    return [u, k * Ca**2]

# Use Shooting Method Solver
def Solver(uGuess):
    # Solve for the Guess Using uGuess
    yGuess = solve_ivp(dfdx, (-xEnd, xEnd), [Ca0, uGuess[0]], t_eval=np.linspace(-xEnd, xEnd, 100))
    
    # Plot each guess for visual inspection
    plt.plot(yGuess.t, yGuess.y[0], label=f"Guess: u={uGuess[0]:.5f}")
    
    return yGuess.y[1, -1]  # Return the derivative at xEnd

# Make an Initial Guess (Magic Number)
uGuessInit = [-1]

# Solve for the Correct U
correctU = fsolve(Solver, uGuessInit, xtol=10**(-12))

print(correctU)

# Plot the solution with the correct U
yFinal = solve_ivp(dfdx, (xInit, xEnd), [Ca0, correctU[0]], t_eval=np.linspace(xInit, xEnd, 100))
plt.plot(yFinal.t, yFinal.y[0], 'k--', label=f"Final Solution: u={correctU[0]:.5f}", linewidth=2)

plt.xlabel('Position, x (cm)')
plt.ylabel('Concentration, $C_A$ (mol/cm$^3$)')
plt.title('Concentration Profile of Species A with Shooting Method')
plt.legend()
plt.grid(True)
plt.show()
