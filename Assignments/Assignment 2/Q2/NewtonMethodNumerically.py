import numpy as np
from time import perf_counter
#Newton Method Numerically
def SystemOfEquations(variables):
    Jc, Jh, Tc, Th = variables
    return np.array([
        5.67e-8 * Tc**4 + 17.41 * Tc - Jc - 5188.18,
        Jc - 0.71 * Jh + 7.46 * Tc - 2352.71,
        5.67e-8 * Th**4 + 1.865 * Th - Jh - 2250,
        Jh - 0.71 * Jc + 7.46 * Th - 11093
    ])

def NumericalJacobian(funcs, variables, stepSize):
    n = len(variables)
    J = np.zeros((n, n))
    
    for i in range(n):
        perturbedVariables = variables.copy()
        perturbedVariables[i] += stepSize
        fp = funcs(perturbedVariables)
        
        perturbedVariables[i] = variables[i] - stepSize
        fm = funcs(perturbedVariables)
        
        J[:, i] = (fp - fm) / (2 * stepSize)
    
    return J

def NewtonMethod(f, x0, tol=1e-4, maxIter=100):
    x = np.array(x0, dtype=float)
    for i in range(maxIter):
        func = f(x)
        jacobian = NumericalJacobian(f, x, 1e-5)
        deltaX = np.linalg.solve(jacobian, -func)
        newX = x + deltaX
        if np.all(np.abs(newX - x) < tol * np.abs(newX)):
            return newX, i + 1
        x = newX
    return x, maxIter

initialValues = [3000, 5000, 298, 298]
startTime = perf_counter()
solutionNewton, iterationsNewton = NewtonMethod(SystemOfEquations, initialValues)
timeNewton = perf_counter() - startTime

print("\n")
print(f"Newton Numerically Solution : {solutionNewton}")
print(f"Newton Numerically Iterations : {iterationsNewton}")
print(f"Newton Numerically Time : {timeNewton}")
print("\n")
