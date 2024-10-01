#example 1 shooting method now solved with builtin solvers
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

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
# solve using solve_ivp  #
# ====================== #
#lets now use a builtin methods to solve the ODE

#first guess at u
u_guess1=10
T_guess1 = solve_ivp(dfdx,(x0,xend),[T_x0,u_guess1])
#lets look at shape for the solution
print('-'*10)
print(T_guess1.y.shape,T_guess1.t.shape)
print('-'*10)
#so rows are T and dTdx
#col are time
T_end_guess1 = T_guess1.y[0,-1] #remember sol for solve_ivp has the values in sol.y
								  #we want the T so first col and at last position so row -1
								  #look at the shape of sol.y for more info

#lets check if the T(x=10) matches our BC?
print("with a first guess of dTdx(x=0) =",u_guess1,end=' ')
print("the temperature at  x=",xend,"is",T_end_guess1,"and should be",T_end)

#second guess at u
u_guess2=20
T_guess2 = solve_ivp(dfdx,(x0,xend),[T_x0,u_guess2])
T_end_guess2 = T_guess2.y[0,-1]

#lets check if the T(x=10) matches our BC?
print("with a second guess of dTdx(x=0) =",u_guess2,end=' ')
print("the temperature at  x=",xend,"is",T_end_guess2,"and should be",T_end)

#third guess, interpolate or extrapolate!
#in this case interpolate
#p1(x)=b0+b1(x-x0)
#b1 is the slope of the line 
b1=(T_end_guess1-T_end_guess2)/(u_guess1-u_guess2)
b0= T_end_guess1

#we want the x for which
#p1(x)=T(x=10)=b0+b1(x-x0)
u_guess3=(T_end-b0)/b1+u_guess1

#third (and hopefully final!) guess at u
T_guess3 = solve_ivp(dfdx,(x0,xend),[T_x0,u_guess3])
T_end_guess3 = T_guess3.y[0,-1]

#lets check if the T(x=10) matches our BC?
print("with a third guess of dTdx(x=0) =",u_guess3,end=' ')
print("the temperature at  x=",xend,"is",T_end_guess3,"and should be",T_end)

#points for plotting
x_val=np.linspace(x0,xend,100)

#now lets plot the results against each other 
plt.figure()
plt.subplot(221)
plt.plot(x_val,T_analytical(x_val),'-k',label='analytical')
plt.plot(T_guess1.t,T_guess1.y[0],'ro',label='values from u0='+str(u_guess1))
plt.legend()
plt.xlabel('x')
plt.ylabel('T(x)')

plt.subplot(222)
plt.plot(x_val,T_analytical(x_val),'-k',label='analytical')
plt.plot(T_guess2.t,T_guess2.y[0],'bo',label='values from u0='+str(u_guess2))
plt.legend()
plt.xlabel('x')
plt.ylabel('T(x)')

plt.subplot(212)
plt.plot(x_val,T_analytical(x_val),'-k',label='analytical')
plt.plot(T_guess3.t,T_guess3.y[0],'go',label='values from u0='+str(round(u_guess3,4)))
plt.legend()
plt.xlabel('x')
plt.ylabel('T(x)')
plt.show()