import numpy as np
from scipy.linalg import lu_factor, lu_solve
import matplotlib.pyplot as plt

#BC values 
Tleft=100
Tright=50
Tinitial=0

#spacing for x
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

#row 0 of T holds temperature values at t0=0
#row 1 holds values at t=t0+dt
#row 2 holds values at t=t0+2*dt
#we need n rows, m columns
#could have been other way around
T=np.zeros((total_nodes_t,total_nodes_x))

#IC
T[0,1:-1]=Tinitial #IC was zero so not needed but just in case


#BCs
#col 1 holds values at left side of the rod
#last col holds the other boundary 
T[:,0]=Tleft
T[:,-1]=Tright

A=np.diag(2*(1+lam)*np.ones(total_nodes_x-2))+\
  np.diag(-lam*np.ones(total_nodes_x-3),1)+\
  np.diag(-lam*np.ones(total_nodes_x-3),-1)
  
print("A= \n",A)

#let's make the b for the first step and compare to our hand solution
#step 1 figure this out
#row 0 holds values of T(t=0)
#for l=1 we need T(l=0)
b=np.zeros(total_nodes_x-2) 


#b[0]=lamT[0,0]+2(1-lam)T[0,1]+lamT[0,2]   +lam T[1,0] (left BC)
#b[1]=lamT[0,1]+2(1-lam)T[0,2]+lamT[0,3]   
#b[2]=lamT[0,2]+2(1-lam)T[0,3]+lamT[0,4]   
#b[3]=lamT[0,3]+2(1-lam)T[0,4]+lamT[0,5]   +lam T[1,5] (right BC)

#---------------gen pattern-------------
#b[i]=lamT[0,i]+2(1-lam)T[0,i+1]+lamT[0,i+2]
#b=lam*T[0,0:-2]+2(1-lam)*T[0,1:-1]+lam*T[0,2:]

#note that this is vectorized and can be done with another for loop
b=lam*T[0,0:-2]+2*(1-lam)*T[0,1:-1]+lam*T[0,2:]

print("b initial =\n",b)
#now modify first and last values for B
# b[0]+=lam*Tleft
# b[-1]+=lam*Tright

#or 
#t=0 so row is 0
#left BC-> col 0 for T
b[0]+=lam*T[0,0]
b[-1]+=lam*T[0,-1]

#let's check this b against hand soln
print("b final =\n",b)

#solve using lu 
#factor A
lu, piv = lu_factor(A)#this doesnt change 
X = lu_solve((lu, piv), b)#only b changes 

print("solution for row 1 of T =\n",X)

#step 2
#check we get the same result
T[1,1:-1]=X

print("first two rows of T after subs=\n",T[:2])

#step3 extend for other steps in time
#we have already solved for l=1
#A remains the same 
#only b changes

for l in range(1,total_nodes_t-1):
	b=lam*T[l,:-2]+2*(1-lam)*T[l,1:-1]+lam*T[l,2:]
	b[0]+=lam*T[l,0]
	b[-1]+=lam*T[l,-1]
	T[l+1,1:-1] = lu_solve((lu, piv), b)
	
#---------------------------------------#
#note that the complete code can be written as

# for l in range(total_nodes_t-1):
# 	b=lam*T[l,:-2]+2*(1-lam)*T[l,1:-1]+lam*T[l,2:]
# 	b[0]+=lam*T[l,0]
# 	b[-1]+=lam*T[l,-1]
# 	T[l+1,1:-1] = lu_solve((lu, piv), b)

#but it is good practice to break the 
#code apart and try it out one part at
#a time
#-----------------------------------------#



#------Note-----
#CN is Uncoditionally stable but may show oscillations if dt*k/dx**2 
#is greater than 1/2
ratio = dt*k/dx**2
if ratio >0.5:
	print(f' Warning, ratio is {ratio} oscillations might be seen ')

#same plot as before
plt.figure()
snap1=30
snap2,snap3=2*snap1,3*snap1

plt.plot(x_val,T[snap1,:])
plt.plot(x_val,T[snap2,:])
plt.plot(x_val,T[snap3,:])
plt.xlabel("x")
plt.ylabel("T")
plt.title("T as a function of position")

plt.legend(['t = '+str(t_val[snap1]) + ' s',\
			   't = '+str(t_val[snap2]) + ' s','t = '+str(t_val[snap3])+ ' s'])