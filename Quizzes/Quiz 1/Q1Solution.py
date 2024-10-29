import numpy as np
from scipy.optimize import fsolve

def equations(vars):
    x, y = vars
    eq1 = x**4 + 2*x*y**2 - 4
    eq2 = x**3*y - 4*y - 1
    return [eq1, eq2]

#  Solution 1 
initial_guess = [0, 1.41421]  # You may need to try different values if this doesn't converge
solution = fsolve(equations, initial_guess)
print(f"The solution is x = {solution[0]}, y = {solution[1]}")

# Solution 2
initial_guess = [-1.41421, 0]  # You may need to try different values if this doesn't converge
solution = fsolve(equations, initial_guess)
print(f"The solution is x = {solution[0]}, y = {solution[1]}")