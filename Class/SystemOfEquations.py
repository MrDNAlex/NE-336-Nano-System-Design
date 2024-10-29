import numpy as np
import scipy

AVals = [[3 , -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]]
bVals = [[7.85], [-19.3], [71.4]]
bVals2 = [[7.85, -19.3, 71.4]]

A = np.array(AVals)
b = np.array(bVals2).T

print(A)
print(b)

AugmentMatrix = np.concatenate((A,b), axis = 1)
#AugmentMatrix2 = np.hstack((A, b))

print(AugmentMatrix)
#print(AugmentMatrix2)

solve = np.linalg.solve(A, b)

print(solve)


# LU Decomposition
from scipy.linalg import lu_factor, lu_solve, lu

P, L, U = lu(A)

print("P=", P)
print( "L=", L)
print( "U=", U)

d = np.linalg.solve(L, b)

x_lu = np.linalg.solve(U, d) # this is solution

print(x_lu)

# builtin 
x_lu_builtin = lu_solve(lu_factor(A), b)

print(x_lu_builtin)




# Non linear Equations (Jacobian)


import scipy.optimize


A = np.array([[6.5, 1.5], [36.75, 32.5]]) # Jacobian

b = np.array([[2.5], [-1.625]])

xo = np.array([[1.5], [3.5]])

print(A)
print(b)

solve = np.linalg.solve(A, b) # Delta X and Delta Y

print(solve)

newB = solve + xo

print(newB)



# Correct way to input functions 

def func_try (z):
    
    #Split if you want, or we can directly index
    [x,y] = z
    
    f = [x**2 + x*y - 10, y + 3*x*y**2 -57]
    
    return f


print(scipy.optimize.fsolve(func_try, [1.5, 3.5]))

