import numpy as np
import matplotlib.pyplot as plt

#spacing for x
#try changing this afterwards
dx=2
(x0,xend)=(0,10)
total_nodes_x=int((xend-x0)/dx + 1) #number of points in x
x_val=np.linspace(x0,xend,total_nodes_x)


#spacing for t
dt=0.1
(t0,tend)=(0,400)
total_nodes_t=int((tend-t0)/dt + 1) #number of points in t
t_val=np.linspace(t0,tend,total_nodes_t)


#BCs
Tleft=100
Tright=50


#lambda=k delt/delx^2
k=0.835# cm^2 /s
lam=k*dt/dx**2

#row 1 of T holds temperature values at t0=0
#row 2 holds values at t=t0+dt
#row 3 holds values at t=t0+2*dt
#we need n rows, m columns
#could have been other way around
T=np.zeros((total_nodes_t,total_nodes_x))

#IC
#T=0
#T[0,1:-1]=0


#BCs
#col 1 holds values at left side of the rod
#last col holds the other boundary 
T[:,0]=Tleft
T[:,-1]=Tright

#print to see what T looks like
print(T)


#question
#do the order of the loops matter??

#m is for x
#n is for t 

#fill this out!

for l in range(total_nodes_t-1):    
    for i in range(1,total_nodes_x-1):
        T[l+1,i]=T[l,i]+lam*(T[l,i+1]-2*T[l,i]+T[l,i-1])

print(T)
for i in range(total_nodes_x):
	print(f"The values at time {t_val[2]} for node {i} is {T[2,i]}")

plt.figure()
#I'd like a snapshot of T(x) at these times
snap1=100#update this to get new plot!
snap2,snap3=2*snap1,3*snap1

plt.plot(x_val,T[snap1,:])
plt.plot(x_val,T[snap2,:])
plt.plot(x_val,T[snap3,:])
plt.xlabel("x")
plt.ylabel("T")
plt.title("T as a function of position (explicit)")

plt.legend(['t = '+str(t_val[snap1]) + ' s',\
			   't = '+str(t_val[snap2]) + ' s','t = '+str(t_val[snap3])+ ' s'])