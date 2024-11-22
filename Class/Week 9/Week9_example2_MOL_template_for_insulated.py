import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


#parameters
k=0.835#cm2/s
L=10#cm
Tinit=0#degC, T at time 0
Tleft=100#degC, T at x=0
Tright=50#degC, T at x=L
n=10#number of internal nodes, we will find dx based on this
tstop=200#time to stop at

#determine dx
dx=L/(n+1)
#you can either decide the dx to have the number of nodes be found 
#or decide on n to have dx found


#ODE function
def dTdt(t,T):
    
    #T=[T0, T1, T2, T3]
	
    T_all=                  #-----FILL-----
    
    dT= np.zeros(T.size)
    
    dT[0] =                 #-----FILL-----
	
    dT[1:]=T_all[2:]-2*T_all[1:-1]+T_all[0:-2]
	
	#multiply by lambda
    lam=k/dx**2
	
    return lam*dT


	
#what is the IC to provide to solve_ivp?
T_init=Tinit*np.ones(n+1)
#Tinit is now an array of the initial value 
#for the internal nodes


#solve
solution=solve_ivp(dTdt,[0,tstop],T_init)
	
print(solution.y.shape)
#so each row is one of the nodes 
#each column is a new time


tsteps = solution.t.size
time = solution.t #the times

#add in the BCs back 
sol=np.vstack([  solution.y,
			     Tright*np.ones(tsteps)])

#lets print some results
print("T at t =",time[0])
print(sol[:,0])
print("T at t =",time[-1])
print(sol[:,-1])

#x values for the plot
x_val=np.linspace(0,L,n+2)
#lets try a simple plot 
plt.figure()
for i in range(tsteps):
	plt.cla()
	plt.ylim([0,120])
	plt.plot(x_val,sol[:,i],label='t='+str(time[i])+'s')
	plt.legend()
	plt.xlabel("x")
	plt.ylabel("T")
	plt.pause(0.1)
plt.show()

