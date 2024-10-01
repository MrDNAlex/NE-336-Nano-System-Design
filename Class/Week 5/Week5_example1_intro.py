#example 2 shooting method
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

Tinf=20 #deg C
T_x0=40 #deg C
T_end=200 #deg C
hp=0.01#/m2

def dfdx(x,f):
    #f is the vector [T,u]
    #where u is dTdx
    #so dfdx is [u,h'(T-Tinf)]
    [T,u]=f
    #write dfdx with me
    df=[u,hp*(T-Tinf)]
    return df

#lets use solve_ivp as start to see how the guess affects outcome

guess=10
sol=solve_ivp(dfdx,(0,10),[T_x0,guess])

print(f'with guess of {guess}, the temperature at end is {sol.y[0,-1]:.3f} and it should be {T_end}')