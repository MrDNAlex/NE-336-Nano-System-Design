import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
def dxdt(t,x):
	#x is a an vector holding x1 and x2
	#it will be a row vector 
	#so x=[x1,x2]
	
	dxdt_array = np.zeros((2,))
	dxdt_array[0]=-0.5*x[0]
	dxdt_array[1]=4-0.3*x[1]-0.1*x[0]
	
	return dxdt_array

x0=np.array([4,6])#vector of ICs

#set up 
delt=0.05
(t0,tend)=(0,2)
n=int((tend-t0)/delt + 1) #find number of points
t_val=np.linspace(t0,tend,n)#t values 

#euler 
#so xi+1=xi +f(ti,xi)*dt
x_euler=np.zeros((n,2))#each row is a new t!
x_euler[0,:]=x0 #IC

for i in range(1,n):
	x_euler[i,:]=x_euler[i-1,:]+dxdt(t_val[i-1],x_euler[i-1,:])*delt
	
print(x_euler)


#solve for rk4 based on this!




want_plot=True
#solve ivp
#write here


if want_plot:
	plt.figure()
	plt.plot(t_val,x_euler[:,1],'k-',label='x2 from euler')
	#plt.plot(,label='x2 from solve_ivp')#complete 
	plt.legend()
	plt.show()