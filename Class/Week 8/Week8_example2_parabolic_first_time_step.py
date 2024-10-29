import numpy as np
from scipy.linalg import lu_factor,lu_solve
np.set_printoptions(precision=4,suppress=True)

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

#row 1 of T holds temperature values at t0=0
#row 2 holds values at t=t0+dt
#row 3 holds values at t=t0+2*dt
T=np.zeros((total_nodes_t,total_nodes_x))

#IC
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
  
print("A =",A,sep="\n")

#since A doesnt change, we can use LU
lu, piv = lu_factor(A)

#let's make the b for the first step and compare to our hand solution



#step 1 

#we need IC for all interior nodes to build b
#row 1 of our T array holds values of T(t=0)
print('---'*10)
print(T[0,1:-1]) #<----- Ti for all interior nodes at t=0
print('---'*10)

#step 2, lets copy these values into b
b=np.copy(T[0,1:-1])           

#step 3 : add in the two BCs to first and last row of b
b[0]+=lam*Tleft                    
b[-1]+=lam*Tright                 
print('---'*10)
print("b after applying BCs")
print(b)
print('---'*10)


#now solve for T at l=1
X=lu_solve((lu, piv),b)


#step 2
#check we get the same result
T[1,1:-1]=X

#print(T[:2])

#now this solves for l=1, how to extend?
