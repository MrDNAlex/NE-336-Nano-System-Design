import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib import cm
 
def dTdt(t,T,p):
	#all parameters will be passed through p
	#which is a dictionary

	T_all=np.hstack([p['Tleft'],T,p['Tright']])
	
	
	dT=T_all[2:]-2*T_all[1:-1]+T_all[:-2]
	
	#multiply by lambda
	lam=p['k']/p['dx']**2
	
	return lam*dT


#note that any changes to the parameters can be made right here!
par={'k':0.835,'L':10,'Tinit':0,'Tleft':100,'Tright':50,
	    'n':20,'tstop':100,'tsteps':201 }

dx=par['L']/(par['n']+1)#find dx
#add it to the dictionary
par['dx']=dx
	
	
#IC for solve_ivp
Tinit=par['Tinit']*np.ones(par['n'])
	
#times solved for
time=np.linspace(0,par['tstop'],par['tsteps'])
	
#solve
sol1=solve_ivp(dTdt,[0,par['tstop']],Tinit,args=(par,),t_eval=time)
	
#add in the BCs back 
sol=np.vstack([par['Tleft']*np.ones(sol1.t.size),sol1.y,par['Tright']*np.ones(sol1.t.size)])
	


#plots!

#lets make sub plots
#------------plot1---------------
#add the one from before as the first one
x_val=np.linspace(0,par['L'],par['n']+2)

fig = plt.figure()

#plot for all x so all rows
axs = fig.add_subplot(2, 2, 1)
axs.plot(x_val,sol[:,0])#first time
axs.plot(x_val,sol[:,par['tsteps']//8])
axs.plot(x_val,sol[:,par['tsteps']//4])
axs.plot(x_val,sol[:,par['tsteps']//2])#mid time interval
axs.plot(x_val,sol[:,-1])#last time
axs.set_xlabel("x")
axs.set_ylabel("T")
axs.set_title("T as a function of position")

axs.legend(['t = '+str(time[0]) + ' s',\
				    't = '+str(time[par['tsteps']//8]) + ' s',
				   't = '+str(time[par['tsteps']//4]) + ' s',
				   't = '+str(time[par['tsteps']//2]) + ' s',
				   't = '+str(time[-1])+ ' s'])
	
	
#------------plot2---------------
#we can plot each node as a function of time!
axs = fig.add_subplot(2, 2, 2)
axs.plot(time[::10],sol[0,:][::10],'r--*',label='node 0')#first node
axs.plot(time[::10],sol[-1,:][::10],'b--*',label='node'+str(par['n']+2))#last node
for i in range(1,par['n']+2,5):
	axs.plot(time,sol[i,:],label='node'+str(i))
axs.set_xlabel("t(s)")
axs.set_ylabel("T")
axs.set_title("T as a function of time at various nodes")
axs.legend()


#------------plot3---------------
#we could try a 3d plot!
time2d,x2d = np.meshgrid(time,x_val)

axs = fig.add_subplot(2, 2, 3, projection='3d')
surf=axs.plot_surface(x2d,time2d,sol,cmap=cm.jet, linewidth=0,
                antialiased=False)
plt.colorbar(surf, shrink=0.5, aspect=5,pad=0.2)
axs.set_xlabel('x')
axs.set_ylabel('t')
axs.set_zlabel('T(t,x)')


#------------plot4---------------
#lets add in an animation!
axs = fig.add_subplot(2, 2, 4)
for i in range(0,par['tsteps'],10):
	plt.cla()
	axs.set_ylim([0,120])
	axs.plot(x_val,sol[:,i],label='t='+str(time[i])+'s')
	axs.legend()
	axs.set_xlabel("x")
	axs.set_ylabel("T")
	plt.pause(0.1)
plt.show()






