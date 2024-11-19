import numpy as np
import matplotlib.pyplot as plt

#BC values 
Tleft=100
Tright=50
Tinitial=0

#spacing for x
dx=0.6
(x0,xend)=(0,10)
total_nodes_x=int((xend-x0)/dx + 1) #number of points in x
x_val=np.linspace(x0,xend,total_nodes_x)


#spacing for t
dt=0.1
(t0,tend)=(0,12)
total_nodes_t=int((tend-t0)/dt + 1) #number of points in t
t_val=np.linspace(t0,tend,total_nodes_t)

#lambda=k delt/delx^2
k=0.835# cm^2 /s
lam=k*dt/dx**2


#Set up T
T=np.zeros((total_nodes_t,total_nodes_x))

#IC
T[0,1:-1]=Tinitial


#BCs
T[:,0]=Tleft
T[:,-1]=Tright

for l in range(total_nodes_t-1):    
    for i in range(1,total_nodes_x-1):
        T[l+1,i]=T[l,i]+lam*(T[l,i+1]-2*T[l,i]+T[l,i-1])



#plot 
plt.figure()
snap1=40
snap2,snap3=2*snap1,3*snap1

plt.plot(x_val,T[snap1,:])
plt.plot(x_val,T[snap2,:])
plt.plot(x_val,T[snap3,:])
plt.xlabel("x")
plt.ylabel("T")
plt.title("T as a function of position")

plt.legend(['t = '+str(t_val[snap1]) + ' s',\
			   't = '+str(t_val[snap2]) + ' s','t = '+str(t_val[snap3])+ ' s'])
plt.show()