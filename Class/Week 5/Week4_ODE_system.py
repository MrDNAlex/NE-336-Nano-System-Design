import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


#IMPORTANT NOTE: even though t isnt in the RHS, you need to include it as the first arg    
#alternatively you can put _ instead of t and write dxdt(_,x)    
    
def dxdt(t,x):
    
	#x is a an vector holding x1 and x2
	#it will be a row vector 
	#so x=[x1,x2]
	
	dxdt_array = np.zeros((2,))
	print(dxdt_array)
	dxdt_array[0]=-0.5*x[0]
	dxdt_array[1]=4-0.3*x[1]-0.1*x[0]
	
	return dxdt_array

x0=np.array([4,6])#vector of ICs

#set up 
delt=0.5
(t0,tend)=(0,2)
n=int((tend-t0)/delt + 1) #find number of points
t_val=np.linspace(t0,tend,n)#t values 

#euler 
#so xi+1=xi +f(ti,xi)*dt
x_euler=np.zeros((t_val.size,2))#each row is a new t!
x_euler[0,:]=x0 #IC

for i in range(1,n):
	x_euler[i,:]=x_euler[i-1,:]+dxdt(t_val[i-1],x_euler[i-1,:])*delt
	
print(x_euler)


#solve for rk4 based on this!
#solve ivp
#write here



want_plot=True


if want_plot:
    plt.figure()
    plt.plot(t_val,x_euler[:,0],'k-',label='from euler')
    #plt.plot(,'r.',label='from solve_ivp') #<-------complete 
    plt.title('$x_1$')
    plt.legend()
    plt.show()