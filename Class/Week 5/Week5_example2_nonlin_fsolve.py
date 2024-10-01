#example 2 shooting method
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp

Ta=20 #deg C
T_x0=40 #deg C
T_end=200 #deg C
hpp=5e-8#/m2
(x0,xend)=(0,10)


def dfdx_nl(x,f):
    #f is the vector [T,u]
    #where u is dTdx
    #so dfdx is [u,h'(T-Tinf)]
	
    dfdx_vals=[0,0]
    dfdx_vals[0]=f[1] #this is u
    dfdx_vals[1]=hpp*(Ta-f[0])**4
	
    return dfdx_vals


def for_solver(u_guess):
    #this function only needs to take in the u0 that we guess
    #and we just need to set up the whole problem as a zero finding one
	 
    #all our previous steps just go under this function
    T_guess = solve_ivp(dfdx_nl,(x0,xend),[T_x0,u_guess[0]])
	
    print(f"for the guess of u={ u_guess[0]:.10f}")
    print(f"The temperature at the end is {T_guess.y[0,-1]:.5f} and should be {T_end}")
	
    #Now what we need to be zero is T_guess.y[0,-1]-T_end
    return T_guess.y[0,-1]-T_end

if __name__=="__main__":
	
    #here is the shooting part!
    #lets first try out a u0
    u_guess1=[9.5]
    #what does the function return ?
    print(for_solver(u_guess1))
	
    #if this was zero, we would have our correct u0
    #to find it, we use a general nonlinear solver
    correct_u=fsolve(for_solver,u_guess1)
    print(f'The correct value for u is {correct_u} ')
    #the returned value from fsolve is an array
	
    #now lets get our data back 
    T_IC= [T_x0,correct_u[0]]
    T= solve_ivp(dfdx_nl,(x0,xend),T_IC)
	
	
    print("T values from the solve_ivp method")
    print(T.y[0])
	
	
