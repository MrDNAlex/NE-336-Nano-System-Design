import numpy as np

n=4
A1=np.diag(2*np.ones(n))

#lets see what diag makes 
print(A1)
print('-'*20)

#what if we provide an additional input?
A2=np.diag(-1*np.ones((n-1)),-1)
A3=np.diag(3*np.ones((n-1)),1)
print(A2,A3, sep='\n')

#how do we make it all into one matrix?
A1+=A2+A3
print('-'*20)
print(A1)


#now that we have practiced, lets make the A for our system

#total number of nodes
m=6

#make A using diag 



#make b 


#now lets make the entire solution
T=np.zeros(m)

#BCs
T[0]= 40
T[-1]=200
print(T)
#T[1:-1]=np.linalg.solve(A,b)

#print(T)
#for i in range(m) :
#	print("The temperature at node",i,"is",T[i])