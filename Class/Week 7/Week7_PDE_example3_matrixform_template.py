import numpy as np 

#nodes in x direction
m=3

#nodes in y dir 
n=3

#T values for boundaries
T_right=50
T_left=75
T_top=100


#We need three additional nodes at the bottom
#so we will have one more row at the bottom
k=(n+1)*m
# we have -4 on the diagonal and one on the lower and upper off diag. 
#FILL

#lets check A
#print(A)

#now add in the zeros 
#FILL
#for i in :
#	A[i+1,i]=0
#	A[i,i+1]=0


#lets check A again

# print('-'*50)
# print(A)
# print('-'*50)

#now +1 on diag+2 and diag -2 except a few 2 at the top
#lets first make the +1
#FILL this out as C and add it in 
#C=
#print(A+C)
#A+=C

#now let's put in the 2 s
# A[0,3]=2
# A[1,4]=2
# A[2,5]=2

# #final look at A
# print('-'*50)
# print(A)


#now lets build b 
b=np.zeros(k)
b[0::3]=-T_left
b[2::3]=-T_right
#check b 
#print(b)

#now -100 of the last three
b[-3:]-=T_top

#check b 
#print(b)

#change this when ready to solve
ready_to_solve=False

if ready_to_solve:

	#solve for T    
	T_solve=np.linalg.solve(A,b)

	#Now assign to T matrix
	T=np.zeros((n+2,m+2))
	T[:,0]=T_left
	T[0,:]=T_top
	T[:,-1]=T_right
	print(T)

	#first three values are the last row of T 
	T[-1,1:-1]=T_solve[:3]
	print(T)
	#second three values are the row above 
	T[-2,1:-1]=T_solve[3:6]
	print(T)
	#so on 
	T[-3,1:-1]=T_solve[6:9]
	T[-4,1:-1]=T_solve[9:]

	print(T)
	#Ofcourse these lines can be written much better but I leave that up to
	#you!
