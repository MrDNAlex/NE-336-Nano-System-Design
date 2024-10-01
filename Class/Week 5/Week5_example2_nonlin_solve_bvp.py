#example 2 shooting method
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp,solve_bvp

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


def for_solver(u_guess):
    #this function only needs to take in the u0 that we guess
    #and we just need to set up the whole problem as a zero finding one
	 
    #all our previous steps just go under this function
    T_guess = solve_ivp(dfdx_nl,(x0,xend),[T_x0,u_guess[0]])
	
    #Now what we need to be zero is T_guess.y[0,-1]-T_end
    return T_guess.y[0,-1]-T_end

def MyBcs(T_0,T_L):
	
    BC1=T_0[0]-T_x0
    BC2=T_L[0]-T_end
	
    return [BC1,BC2]
	
if __name__=="__main__":
	
    #here is the shooting part!
    #lets first try out a u0
    u_guess1=5
	
    #if this was zero, we would have our correct u0
    #to find it, we use a general nonlinear solver
    correct_u=fsolve(for_solver,u_guess1)
	
    #the returned value from fsolve is an array
	
    #now lets get our data back 
    T_IC= [T_x0,correct_u[0]]
    T= solve_ivp(dfdx_nl,(x0,xend),T_IC,t_eval=np.linspace(x0,xend,100))
	
	
    print("T values from the solve_ivp method")
    print(T.y[0])
	
	
    #now solve_bvp 
    x_=np.linspace(x0,xend,100)
    y_=np.zeros((2,x_.size))
    sol=solve_bvp(dfdx_nl,MyBcs,x_,y_)
	
	
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('x ')
    ax1.set_ylabel('T', color=color)
    ax1.plot(T.t,T.y[0], color=color,linewidth=2,label='shooting method')
    ax1.plot(sol.x,sol.y[0],'k-.',label='solve_bvp')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc=2)
		
		
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
	
    color = 'tab:blue'
    ax2.set_ylabel('dT/dx', color=color)  # we already handled the x-label with ax1
    ax2.plot(T.t,T.y[1], '*',color=color,linewidth=2,label='shooting method')
    ax2.plot(sol.x,sol.y[1],'k-.',label='solve_bvp')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc=4)
		
    #change to solution to have dTdx(x=L)=0 as second BC