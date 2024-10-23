import numpy as np 

T_left=75
T_top=100
T_right=50

#interior nodes in x direction
m=3

#interior nodes in y dir 
n=3

#matrix holding T values is 5X5 with the BCs
T=np.zeros((n+2,m+2)) 

#over relax factor
lam=1.5 


#help me put BCs in their places

T[:,0]= T_left
T[0,:]= T_top
T[:,-1]= T_right
#T[-1,:]= T_bot

print(T)

#how many times run?
k=0
error = 100*np.ones(T.shape)

while k < 100 and np.max(error[1:-1,1:-1]) > 1e-2:
	for row in range(n, 0, -1): 
		for col in range(1, m+1) :
			
			old = T[row, col]
	
			T[row,col]=0.25*(T[row+1,col]+T[row-1,col]+T[row,col+1]+T[row,col-1]) 
			T[row,col]=lam*T[row,col]+(1-lam)*old
			error[row, col] = abs(T[row, col] - old)/T[row, col]
	k += 1
		                 

print("The temperature distribution within the plate is:")
print(T)
# for i in range(1,n+1):
	# print(T[i,1:m+1])





