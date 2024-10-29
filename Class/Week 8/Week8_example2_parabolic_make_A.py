import numpy as np

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
(t0,tend)=(0,12)
total_nodes_t=int((tend-t0)/dt + 1) #number of points in t
t_val=np.linspace(t0,tend,total_nodes_t)


#lambda=k delt/delx^2
k=0.835# cm^2 /s
lam=k*dt/dx**2


#fill this out
A=
  
print(A)