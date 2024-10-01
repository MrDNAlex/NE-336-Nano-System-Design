# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:52:00 2024

@author: a3dufres
"""

# Alexandre Dufresne-Nappert
# 20948586

import numpy as np
import scipy as sp


# Need to iterate using newton raphson to get initial guesses


#Finding Roots

xs1 = 1
xs2 = 2

xn1 = xs1 - f1(xs1, xs2) /  





f1 = lambda x, y: x**4+2*x*y**2 - 4 # = 0

f2 = lambda x, y: (x**3)*y-4*y-1 # = 0


result = np.linalg.solve(a, b)


df1x =  lambda x, y: 4*x**3+2*y**2
df1y = lambda x, y: 4*x*y

df2x = lambda x, y: 3*(x**2)*y
df2y = lambda x, y: (x**3)-4

# x, y
xo = [1, 1]


A = np.zeros((2, 2))

A[0, 0] = df1x(xo[0], xo[1])
A[0, 1] = df1y(xo[0], xo[1])
A[1, 0] = df2x(xo[0], xo[1])
A[1, 1] = df2y(xo[0], xo[1])


print(A)

b = np.array([ [4], [1]])

print(b)


result = np.linalg.solve(A, b)

print(f"Result : {result}")

# df1 / x       df1 / y

# df2 / x       df2 / y 




#result = np.linalg.solve(a, b)





