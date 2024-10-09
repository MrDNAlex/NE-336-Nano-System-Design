import numpy as np
from scipy.optimize import fsolve
from time import perf_counter

# FSolve Method
def SystemOfEquations(variables):
    Jc, Jh, Tc, Th = variables
    return [
        5.67e-8 * Tc**4 + 17.41 * Tc - Jc - 5188.18,
        Jc - 0.71 * Jh + 7.46 * Tc - 2352.71,
        5.67e-8 * Th**4 + 1.865 * Th - Jh - 2250,
        Jh - 0.71 * Jc + 7.46 * Th - 11093
    ]


initialValues = [3000, 5000, 298, 298]
start = perf_counter()
solutionFsolve, info, ier, mesg = fsolve(SystemOfEquations, initialValues, full_output=True)
timeFsolve = perf_counter() - start
num_iterations = info['nfev']  # Number of function evaluations
print("\n")
print(f"FSolve Solution : {solutionFsolve}")
print(f"FSolve Solution Time : {timeFsolve}")
print(f"FSolve Iterations : {num_iterations}")
print("\n")