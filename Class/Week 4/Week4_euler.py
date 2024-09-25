import numpy as np
import matplotlib.pyplot as plt

#example 1 
dxdt=lambda t: -2*t**3+12*t**2-20*t+8.5
xreal=lambda t:-0.5*t**4+4*t**3-10*t**2+8.5*t+1
 
delt=0.5 #delta t chosen, try changing this 

(t0,tend)=(0,4)

n=int((tend-t0)/delt + 1) #find number of points!why change to int?

t_val=np.linspace(t0,tend,n)#t values 

xinitial = 1 #initial condition of x at t=0


x_vals=[xinitial]#start list 

for i in range(1,n):
	xnew=x_vals[i-1]+dxdt(t_val[i-1])*delt
	x_vals.append(xnew)

x_vals_arr=np.array(x_vals)

x_vals_true=xreal(t_val) #true x values 

global_error = np.abs((x_vals_true-x_vals_arr)/x_vals_true)*100
print(global_error)
#take smaller step?

plt.figure()
plt.plot(t_val,x_vals_arr,'k-',label='euler with dt='+str(delt))
plt.plot(t_val,x_vals_true,'r:',label='real')
plt.legend()
plt.xlabel('t')
plt.ylabel('x')
plt.show()