import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#example 1 
#dxdt=lambda t: -2*t**3+12*t**2-20*t+8.5
#xreal=lambda t:-0.5*t**4+4*t**3-10*t**2+8.5*t+1


#example 3 
dxdt=lambda t,x : 4*np.exp(0.8*t)-0.5*x
#analytical solution
xreal=lambda t: (4/1.3)*(np.exp(0.8*t)-np.exp(-0.5*t))+2*np.exp(-0.5*t)

delt=1.0 #delta t chosen, try changing this 
(t0,tend)=(0,4)#bounds
x0=2 #IC, x(t=0)

n=int((tend-t0)/delt + 1) #find number of points
t_val=np.linspace(t0,tend,n)#t values 
x_true=xreal(t_val) #real values for error


#initial condition of x at t=0
x_vals=[x0]
local_error=[0]

for i in range(1,n):
	
	k1=dxdt(t_val[i-1],x_vals[i-1])
	k2=dxdt(t_val[i-1]+delt/2,x_vals[i-1]+k1*delt/2)
	k3=dxdt(t_val[i-1]+delt/2,x_vals[i-1]+k2*delt/2)
	k4=dxdt(t_val[i-1]+delt,x_vals[i-1]+k3*delt)
	phi=(k1+2*k2+2*k3+k4)/6
	
	xnew=x_vals[i-1]+phi*delt
	x_vals.append(xnew)
	
	err=abs((x_vals[i]-x_true[i])/x_true[i])
	local_error.append(err)
	
x_vals_arr=np.array(x_vals)


print(local_error)

#lets now solve the same problem using solve_ivp from scipy

plt.figure()

plt.plot(t_val,x_vals_arr,'k-s',label='RK4 with dt='+str(delt))
plt.plot(t_val,x_true,'r--*',label='real')
#plt.plot(,'yo',mfc='w')#add solve_ivp soln here
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.show()

