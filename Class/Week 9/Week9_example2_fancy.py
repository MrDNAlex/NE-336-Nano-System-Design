import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#example 2 but a little bit more fancy! 
#I will use a dictionary to hold and pass the parameters

#for the ODE function,
#we would like to pass the parameters as a dictionary to the ODE function
def dTdt(t,T,p):
	#all parameters will be passed through p
	#which is a dictionary
	
	T_all=np.hstack([p['Tleft'],T,p['Tright']])
	

	dT=T_all[2:]-2*T_all[1:-1]+T_all[:-2]
	
	#multiply by lambda
	lam=p['k']/p['dx']**2
	
	return lam*dT

if __name__=="__main__":

	#you could have defined variables but this is just practice
	#and these dictionaries could be provided from outside of this file 
	#and it would still work !
	
	par={'k':0.835,#cm2/s
		  'L':10,#cm
		  'Tinit':0,#degC, T at time 0
		  'Tleft':100,#degC, T at x=0
		  'Tright':50,#degC, T at x=L
		  'n':10,#number of internal nodes, we will find dx based on this
		  'tstop':30,#time to stop at
		  'tsteps':201#number of steps for time
		  }
	#note that any changes to the parameters can be made right here!
	
	dx=par['L']/(par['n']+1)#find dx
	#add it to the dictionary
	par['dx']=dx
	
	#check the parameters
	print(par)
	
	
	#what is the IC to provide to solve_ivp?
	Tinit=par['Tinit']*np.ones(par['n'])
	#Tinit is now an array of the initial value 
	#for the internal nodes

	#stop for time
	tstop=par['tstop']
	#how many steps in time?
	tsteps=par['tsteps']
	
	#times solved for
	time=np.linspace(0,tstop,tsteps)
	
	#solve
	sol1=solve_ivp(dTdt,[0,tstop],Tinit,args=(par,),t_eval=time)
	
	print(sol1.y.shape)#so each row is one of the nodes 
	#add in the BCs back 
	
	sol=np.vstack([par['Tleft']*np.ones(tsteps),sol1.y,par['Tright']*np.ones(tsteps)])
	
	#lets try a simple plot 
	x_val=np.linspace(0,par['L'],par['n']+2)
	plt.figure()
	#plot for all x so all rows
	plt.plot(x_val,sol[:,0])#first time
	plt.plot(x_val,sol[:,tsteps//2])#mid time interval
	plt.plot(x_val,sol[:,-1])#last time
	plt.xlabel("x")
	plt.ylabel("T")
	plt.title("T as a function of position")

	plt.legend(['t = '+str(time[0]) + ' s',\
				   't = '+str(time[tsteps//2]) + ' s','t = '+str(time[-1])+ ' s'])
	plt.show()


