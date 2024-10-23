import numpy as np 
import matplotlib.pyplot as plt


T_left=75
T_top=100
T_right=50

#nodes in x direction
m=3

#nodes in y dir 
n=3

#matrix holding T values is 5X5 with the BCs
T=np.zeros((n+2,m+2)) 

#over relax factor
lam=1.5 

T[:,0]=T_left 
T[0,:]=T_top 
T[:,-1]=T_right
print(T)

#how many times run?
k=0 
eps=100*np.ones(T.shape)
   
while np.max(eps[1:-1,1:-1])>1e-2 and k<100:  
	for row in range(n,0,-1):
		for col in range(1,m+1):
			old=np.copy(T[row,col])
			T[row,col]=0.25*(T[row+1,col]+T[row-1,col]+T[row,col+1]+T[row,col-1]) 
			T[row,col]=lam*T[row,col]+(1-lam)*old 
			eps[row,col]=np.abs((T[row,col]-old)/T[row,col])
			 
	k+=1	
 
print(f"After {k} iterations")
print("The temperature distribution within the plate is:")
print(T)