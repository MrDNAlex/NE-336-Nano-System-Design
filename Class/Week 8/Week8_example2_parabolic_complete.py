import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu_factor,lu_solve

#BC values 
Tleft=100
Tright=50

#spacing for x
#try changing this afterwards
dx=2 
(x0,xend)=(0,10)
total_nodes_x=int((xend-x0)/dx + 1) #number of points in x
x_val=np.linspace(x0,xend,total_nodes_x)


#spacing for t
dt=0.1
(t0,tend)=(0,40)
total_nodes_t=int((tend-t0)/dt + 1) #number of points in t
t_val=np.linspace(t0,tend,total_nodes_t)


#lambda=k delt/delx^2
k=0.835# cm^2 /s
lam=k*dt/dx**2

#row 1 of T holds temperature values at t0=0
#row 2 holds values at t=t0+dt
#row 3 holds values at t=t0+2*dt
T=np.zeros((total_nodes_t,total_nodes_x))

#----IC----
#first row should be zero 
#T[0,1:-1]=0

#BCs
#col 1 holds values at left side of the rod
#last col holds the other boundary 
T[:,0]=Tleft
T[:,-1]=Tright

#for A
#1+2lam on diag
#-lam on off diag
A=np.diag((1+2*lam)*np.ones(total_nodes_x-2))+\
  np.diag(-lam*np.ones(total_nodes_x-3),1)+\
  np.diag(-lam*np.ones(total_nodes_x-3),-1)


#since A doesnt change, we can use LU
lu, piv = lu_factor(A)


# extend for every step in time
for :          #<---------------------complete this to extend 
	b=np.copy(T[l,1:-1])
	b[0]+=lam*Tleft
	b[-1]+=lam*Tright
	T[l+1,1:-1]=lu_solve((lu, piv),b)
print(T)

plt.figure()
snap1=100
snap2,snap3=2*snap1,3*snap1

plt.plot(x_val,T[snap1,:])
plt.plot(x_val,T[snap2,:])
plt.plot(x_val,T[snap3,:])
plt.xlabel("x")
plt.ylabel("T")
plt.title("T as a function of position (implicit)")

plt.legend(['t = '+str(t_val[snap1]) + ' s',\
			   't = '+str(t_val[snap2]) + ' s','t = '+str(t_val[snap3])+ ' s'])