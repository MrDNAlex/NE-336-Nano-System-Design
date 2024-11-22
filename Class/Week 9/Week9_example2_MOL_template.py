import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#example 2 
#the trick to this example is that we want to solve ODES 
#for the interior nodes but we need the BCs as well so we
#will have to be creative in how we pass the BCs to the ODE

#parameters
k=0.835#cm2/s
L=10#cm
Tinit=0#degC, T at time 0
Tleft=100#degC, T at x=0
Tright=50#degC, T at x=L
n=3#number of internal nodes, we will find dx based on this
tstop=40#time to stop at

#determine dx
dx=L/(n+1)
#you can either decide the dx to have the number of nodes be found 
#or decide on n to have dx found


#ODE function
def dTdt(t,T):
	
    #T=[T1 T2 T3]
    
	#what does T have?
	#Only the internal nodes. 
	#so lets add the BCs to the T we are using here
	T_all=np.hstack([Tleft,T,Tright])
	
	#now we have the BCs in T as well. 
	#lets build the ODEs with T_all
	#we could do the loop from before	
	dT=np.zeros(n)
    
	#remember 
	#dTdt[0]=T[2]-2T[1]+T[0]
	#dTdt[1]=T[3]-2T[2]+T[1]
	#dTdt[2]=T[4]-2T[3]+T[2]
	for i in range(n):
		dT[i]=T_all[i+2]-2*T_all[i+1]+T_all[i]
	
	#or ...
	#this is a vectorized version!
	#much faster since no loop!
	#dT=T_all[2:]-2*T_all[1:-1]+T_all[:-2]
	
	#multiply by lambda
	lam=k/dx**2
	
	return lam*dT
	
#what is the IC to provide to solve_ivp?
T_init=       #-----FILL-----
#Tinit is now an array of the initial value 
#for the internal nodes


#solve
solution=   #-----FILL-----
	
print(solution.y.shape)
#so each row is one of the nodes 
#each column is a new time


#what is the number of timesteps?
tsteps =      #-----FILL-----
#the times from the solution
time = 	#-----FILL-----

#add in the BCs back 
sol=np.vstack([Tleft*np.ones(tsteps),
				  solution.y,
			    Tright*np.ones(tsteps)])
print(sol)
want_plot=False

if want_plot:
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

