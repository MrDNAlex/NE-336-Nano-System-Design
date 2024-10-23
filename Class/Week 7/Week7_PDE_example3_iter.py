import numpy as np 

#nodes in x direction
m=4

#nodes in y dir 
n=4

#matrix holding T values is 5X5 with the BCs
T=np.zeros((n+2,m+2)) 

#over relax factor
lam=1.5 

T[:,0]=75 
T[0,:]=100 
T[:,-1]=50
print(T)

#how many times run?
k=0 
eps=100*np.ones(T.shape)
   
while np.max(eps[1:,1:m+1])>0.001:  
	for row in range(n+1,0,-1):
		for col in range(1,m+1):
			old=T[row,col]
			if row==n+1:#last row is different
				T[row,col]=0.25*(2*T[row-1,col]+T[row,col+1]+T[row,col-1]) 
			else:
				T[row,col]=0.25*(T[row+1,col]+T[row-1,col]+T[row,col+1]+T[row,col-1]) 
			
			T[row,col]=lam*T[row,col]+(1-lam)*old 
			eps[row,col]=np.abs((T[row,col]-old)/T[row,col])
			 
	k+=1
	


print(f"After {k} iterations")
print("The temperature distribution within the plate is:")
print(T)



