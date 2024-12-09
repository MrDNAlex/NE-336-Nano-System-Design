import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#
# Alexandre Dufresne-Nappert
# 20948586
#

# 
# Made some print modifications to figure out time, not sure if the file is needed for submission, but in case I signed it
#

# Figure out the time
print(2200/60)
print(34*60)

rho=940 #kg/m3
k=0.47 #W/mk
cp=3.8e3 #J/kgK
alpha=k/rho/cp
Tend=-10#degC
tend=2200

dr=.001
R=0.1/2 
n=int(R/dr)+1 #total number of points

r=np.linspace(0,R,n)

r_int=r[1:-1]

def dTdt(t,T,method='method1'):
    
    #this code will use either a forward difference (method1)
    #or centered difference (method2) for treating the BC at r=0
	
    if  method=='method1':
        #used by default
        #this implements a forward differnce for node 0
        dT=np.zeros(T.shape)
        T0=(4*T[0]-T[1])/3
        T_all= np.hstack([T0,T,Tend])
        dT=alpha/dr*((1/r_int+1/dr)*T_all[2:]-(2/dr)*T_all[1:-1]+(1/dr-1/r_int)*T_all[:-2])
        
    elif method=='method2':
        #this method uses a centered difference for node 0
        T_all= np.hstack([T,Tend])
    
        dT=np.zeros(T.shape)
    
        dT[0]=6*alpha/dr**2*(T_all[1]-T_all[0])
        dT[1:]=alpha/dr*((1/r_int+1/dr)*T_all[2:]-(2/dr)*T_all[1:-1]+(1/dr-1/r_int)*T_all[:-2])
        
	
	
    return dT

#method1
T_initial_method1=5*np.ones(n-2)
		
sol_method1=solve_ivp(dTdt,(0,tend),T_initial_method1,t_eval=np.linspace(0,tend,100),method='BDF')
T0=(4*sol_method1.y[0]-sol_method1.y[1])/3
T_sol_all_method1=np.vstack([T0,sol_method1.y,Tend*np.ones(sol_method1.t.shape)])


#method2
T_initial_method2=5*np.ones(n-1)
		
sol_method2=solve_ivp(lambda t,T: dTdt(t,T,'method2'),(0,tend),T_initial_method2,t_eval=np.linspace(0,tend,100),method='BDF')
T_sol_all_method2=np.vstack([sol_method2.y,Tend*np.ones(sol_method2.t.shape)])


# Checking for the time where center = 0 degrees
tol = 10**(-5)
count = 0
for i in range(len(T_sol_all_method1[0])):
    if T_sol_all_method1[0, i] < tol:
        print("Sec: ", sol_method1.t[i])
        print("Mins: ", sol_method1.t[i] / 60)
        print(T_sol_all_method1[0, i])

# Plotting
plt.figure()
plt.plot(sol_method1.t/60,T_sol_all_method1[0],'k-',label='method1 (forward)')
plt.plot(sol_method2.t/60,T_sol_all_method2[0],'r--',label='method2 (centered)')
plt.xlabel('t (min) ')
plt.ylabel('T (C)')
plt.legend()
plt.title('T(r=0,t) vs time')
plt.show()