# Non Linear Multi Dimensional Newton Raphson
# AKA Jacobi Method 
# This is functional

import numpy as np

# Define the system of nonlinear equations
def F(x):
    f1 = x[0]**2 + x[1]**2 - 4
    f2 = x[0] * x[1] - 1
    return np.array([f1, f2])

# Define the Jacobian matrix of the system
def J(x):
    j11 = 2 * x[0]
    j12 = 2 * x[1]
    j21 = x[1]
    j22 = x[0]
    return np.array([[j11, j12], [j21, j22]])

# Newton-Raphson method for nonlinear systems
def newton_raphson_multidim(F, J, x0, tolerance=1e-10, max_iterations=100):
    x = np.copy(x0)
    for iteration in range(max_iterations):
        jacobian_matrix = J(x)
        f_val = F(x)
        delta_x = np.linalg.solve(jacobian_matrix, -f_val)  # Solve J(x) * delta_x = -F(x)
        x = x + delta_x
        
        if np.linalg.norm(delta_x, ord=2) < tolerance:  # Check for convergence
            return x, iteration

    raise Exception("Newton-Raphson did not converge")

# Initial guess
x0 = np.array([2.0, 1.0])

# Solve the system using Newton-Raphson
solution, iterations = newton_raphson_multidim(F, J, x0)
print(f"Solution: {solution}, found in {iterations} iterations")

