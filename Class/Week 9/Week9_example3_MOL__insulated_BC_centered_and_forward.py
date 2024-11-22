import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


#example 3 with both centered diff and forward diff approach

#parameters
k=0.835#cm2/s
L=10#cm
Tinit=0#degC, T at time 0
Tright=50#degC, T at x=L
n=3#number of internal nodes, we will find dx based on this
tstop=150#time to stop at

#determine dx
dx=L/(n+1)



#ODE function
def dTdt(t,T,centered=True):
    #the optional argument centered will be used to implement a 
    #centerd diff approach for the BC when True
	
    #we now dont need Tleft since it is no longer known.
    T_all=np.hstack([T,Tright])

	
    if centered:
        #-----------centered diff ------------------#
        #using centered diff approach to deal with BC
        dT=np.zeros(n+1)
        #I am using centered diff here for first node
        dT[0]=2*T_all[1]-2*T_all[0]
        #the interior eqns remain the same
        dT[1:]=T_all[2:]-2*T_all[1:-1]+T_all[:-2]
    else:
        #-----------forward diff ------------------#
        #use forward diff for T0
        
        #T0 is still needed for diff eqn for T1
        
        #so first rebuild it
        #please note that since we are not solving a diff eqn for T0,
        #the first value passed into this function by T, 
        #which then goes into T_all[0] is T1 in this case
        #so based on eqn for T0=(4T1-T2)/3
        T_0= (4*T_all[0]-T_all[1])/3 #build T0!
        
        #add T0 back
        T_all_new=np.hstack([T_0,T_all])
        
        #now dT can access T0 for the first diff eqn!
        dT=T_all_new[2:]-2*T_all_new[1:-1]+T_all_new[:-2]
        
        
    #multiply by lambda
    lam=k/dx**2
	
    return lam*dT


	

#solve
#-----------centered diff ------------------#
#when solving using the centered diff, we have 4 eqns so n+1
sol_cen=solve_ivp(dTdt,[0,tstop],Tinit*np.ones(n+1),t_eval=np.linspace(0,tstop,101))

#-----------forward diff ------------------#
#but when using forward diff, we only solve for interior nodes, so only 3 or n
sol_for=solve_ivp(dTdt,[0,tstop],Tinit*np.ones(n),args=(False,),t_eval=np.linspace(0,tstop,101))	



#build full answer 

#full sol using centered diff
#-----------centered diff ------------------#
#add in the BCs back 
sol_cen_full=np.vstack([ sol_cen.y,#note that the first node is solved as a part of dTdt
				  Tright*np.ones(sol_cen.t.size)])
    
#full sol using forward diff
#-----------forward diff ------------------#
#first BC for all time
T_begin= (4*sol_for.y[0,:]-sol_for.y[1,:])/3
sol_for_full=np.vstack([T_begin,
              sol_for.y,
              Tright*np.ones(sol_for.t.size)])

#x values for the plot
x_val=np.linspace(0,L,n+2)
#lets try a simple plot 
plt.figure()



plt.figure()
for i in range(sol_cen.t.size):
    plt.cla()
    plt.ylim([0,120])
    plt.plot(x_val,sol_cen_full[:,i],label='t='+str(sol_cen.t[i])+'s')
    plt.plot(x_val,sol_for_full[:,i],'r--',label='forward')
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("T")
    plt.pause(0.001)
plt.show()


