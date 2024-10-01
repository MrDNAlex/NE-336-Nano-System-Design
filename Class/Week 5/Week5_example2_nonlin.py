#example 2 shooting method
from scipy.integrate import solve_ivp

Ta=20 #deg C
T_x0=40 #deg C
T_end=200 #deg C
hpp=5e-8#/m2
(x0,xend)=(0,10)

def dfdx_nl(_,f):
    #f is the vector [T,u]
    #where u is dTdx
    #so dfdx is [u,h'(T-Tinf)]
	
    dfdx_vals=[0,0]
    dfdx_vals[0]=f[1] #this is u
    dfdx_vals[1]=hpp*(Ta-f[0])**4
	
    return dfdx_vals

	
#lets use solve_ivp

#first guess at u
u_guess1=5
T_guess1 = solve_ivp(dfdx_nl,(x0,xend),[T_x0,u_guess1])
print(T_guess1.y.shape,T_guess1.t.shape)

#lets check if the T(x=10) matches our BC?
print("with a first guess of dTdx(x=0) =",u_guess1,end=' ')
print("the temperature at  x=",xend,"is",T_guess1.y[0,-1],"and should be",T_end)


#since the equation is not linear, we need to solve it with a solver
#lets write another function to give to builtin solver

