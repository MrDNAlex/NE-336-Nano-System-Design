import numpy as np
from time import perf_counter
# Newtons Method
def SystemOfEquations(variables):
    Jc, Jh, Tc, Th = variables
    return [
        5.67e-8 * Tc**4 + 17.41 * Tc - Jc - 5188.18,
        Jc - 0.71 * Jh + 7.46 * Tc - 2352.71,
        5.67e-8 * Th**4 + 1.865 * Th - Jh - 2250,
        Jh - 0.71 * Jc + 7.46 * Th - 11093
    ]

def Jacobian(variables):
    Jc, Jh, Tc, Th = variables
    
    df1Jc = -1
    df1Jh = 0
    df1Tc = 2.268*10**(-7)*Tc**3 + 17.41
    df1Th = 0
    
    df2Jc = 1
    df2Jh = -0.71
    df2Tc = 7.46
    df2Th = 0
    
    df3Jc = 0
    df3Jh = -1
    df3Tc = 0
    df3Th = 2.268*10**(-7)*Th**3 + 1.865
    
    df4Jc = -0.71
    df4Jh = 1
    df4Tc = 0
    df4Th = 7.46
    
    return np.array([ [df1Jc, df1Jh, df1Tc, df1Th],
                      [df2Jc, df2Jh, df2Tc, df2Th],
                      [df3Jc, df3Jh, df3Tc, df3Th],
                      [df4Jc, df4Jh, df4Tc, df4Th]])

def NewtonMethod (f, J, x0, tol= 10**(-4), maxIter = 100):
    x = np.array(x0)
    for i in range(maxIter):
        func = np.array(f(x))
        jacobian = J(x)
        deltaX = np.linalg.solve(jacobian, -func)
        newX = x + deltaX
        if (max(abs(newX - x)/newX < tol)): # Max is a little trick where if one of the values reach tolerance the whole statement is true
            return newX, i+1
        x = newX
    return x, maxIter

initialValues = [3000, 5000, 298, 298]
startTime = perf_counter()
solutionNewton, iterationsNewton = NewtonMethod(SystemOfEquations, Jacobian, initialValues, tol=1e-4)
timeNewton = perf_counter() - startTime

print("\n")
print(f"Newton Solution : {solutionNewton}")
print(f"Newton Iterations : {iterationsNewton}")
print(f"Newton Time : {timeNewton}")
print("\n")