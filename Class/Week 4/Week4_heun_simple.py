import numpy as np
import matplotlib.pyplot as plt

#example 1 
#dxdt=lambda t,_: -2*t**3+12*t**2-20*t+8.5
#xreal=lambda t:-0.5*t**4+4*t**3-10*t**2+8.5*t+1

#example 2 
dxdt=lambda t,x : 4*np.exp(0.8*t)-0.5*x
xreal=lambda t: (4/1.3)*(np.exp(0.8*t)-np.exp(-0.5*t))+2*np.exp(-0.5*t)#try solving this with sympy!

#we can put the variables we want to change here
delt=1 #delta t chosen
(t0,tend)=(0,4)#bounds
x0=2#IC, x(t=0)

n=int((tend-t0)/delt + 1) #find number of points
t_val=np.linspace(t0,tend,n)#t values 
x_true=xreal(t_val) #real values for error


#initial condition of x at t=0
x_vals=[x0]
local_error=[0]

max_iter=15#maximum number of iterations

for i in range(1,n):
	
	#pred for xnew based on Euler 
	xnew=x_vals[i-1]+dxdt(t_val[i-1],x_vals[i-1])*delt
	x_vals.append(xnew)
	x_vals[i]=x_vals[i-1]+0.5*(dxdt(t_val[i-1],x_vals[i-1])+dxdt(t_val[i],x_vals[i]))*delt
	
	iteration=1
	while iteration < max_iter:
		x_vals[i]=x_vals[i-1]+0.5*(dxdt(t_val[i-1],x_vals[i-1])+dxdt(t_val[i],x_vals[i]))*delt
		iteration +=1
	
	err=abs((x_vals[i]-x_true[i])/x_true[i])
	
	local_error.append(err)
	

x_vals_arr=np.array(x_vals)


print(local_error)


plt.figure()
plt.plot(t_val,x_vals_arr,'k-s',label='Heun with dt='+str(delt))
plt.plot(t_val,x_true,'r--*',label='real')
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.show()