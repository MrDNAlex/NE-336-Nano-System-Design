#example 1 shooting method now solved with builtin solvers
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
# =================== #
# Define parameters   #
# =================== #
# here, we define all the parameters at the top of 
#the file and use them below

Tinf=20 #deg C
T_x0=40 #deg C
T_end=200 #deg C
hp=0.01#/m2
(x0,xend)=(0,10)

def dfdx(x,f):
    #we have to include x for builtin methods 
    #or alternatively write dfdx(_,f) since x isnt in the equations
	
    #f =[T,u] where u is dTdx
    #so dfdx is [u,h'(T-Tinf)]
    dfdx_vals=[0,0]
    dfdx_vals[0]=f[1] #this is u
    dfdx_vals[1]=hp*(f[0]-Tinf)
	
    return dfdx_vals
	
#solve for c1 c2 for analytical solution
A = np.array([[1,1],[np.exp(1),np.exp(-1)]])
b = np.array([T_x0-Tinf,T_end-Tinf])
c = np.linalg.solve(A,b)

#added in the analytical solution
T_analytical=lambda x : c[0]*np.exp(0.1*x)+c[1]*np.exp(-0.1*x)+Tinf

# ====================== #
# solve using solve_bvp  #
# ====================== #

#in this method, we need a separate function to define the BCs
def mybc(Ta,Tb):
    #the first argument is the first boundary
    #the second argument is the last boundary
	
    # inputs Ta = [T(0)  u(0)]'
    #        Tb = [T(L)  u(L)]'

    #BCs have to defined as residuals
    BC1=
    BC2=
	
    resid = [BC1,BC2]
    return resid

#for solve_bvp we also have to define 
#an empty object for it to fill with the solution
#grid for x
x_vals=np.linspace(x0,xend)

#object to be filled with y vals 
#note that the rows are the same as the size of your system 
#this is not optional (unlike solve_ivp)
y_vals=np.zeros((2,x_vals.size))



sol=solve_bvp(dfdx,mybc,x_vals,y_vals)


#lets plot the results 
plt.plot(x_vals,T_analytical(x_vals),'k-',label='analytical')
plt.plot(sol.x,sol.y[0],'r-.',label='values from solve_bvp')
plt.xlabel('x',fontsize=16)
plt.ylabel('T(x)',fontsize=16)
plt.legend()
