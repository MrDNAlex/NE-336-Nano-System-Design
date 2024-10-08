import numpy as np
import matplotlib.pyplot as plt

#constants from the question
Tend = 200
Ta = 20
L = 10
h = 0.01

#number of total nodes
n=6
dx=L/(n-1)

T=np.zeros((n,))
T[-1]=Tend

#making the A matrix

#2+hdx**2 on diad
#-1 on off diag
A=np.diag((2+h*dx**2)*np.ones(n-1))+np.diag(-1*np.ones(n-2),1)+\
  np.diag(-1*np.ones(n-2),-1)
  
#change the value on first row second column
A[0,1]=-2

#lets check A
print(A)

#making b !
#h dx**2 Ta in all terms
#b[-1] has +Tend
b= h*dx**2*Ta*np.ones(n-1)
b[-1]+=Tend


#now solve!
T[:-1]=np.linalg.solve(A,b)

for i in range(n) :
	print("The temperature at node",i,"is",T[i])

#added in the analytical solution
#note : you will need to find this again based on insulated BC
T_analytical=lambda x : Ta+58.325*(np.exp(0.1*x)+np.exp(-0.1*x))

xvals=np.linspace(0,L,2*n-1)
plt.figure()
plt.plot(xvals,T_analytical(xvals),'b-',label='analytical')
plt.plot(xvals[::2],T,'ro',label='FD')
plt.legend()
plt.xlabel('x')
plt.ylabel('T')
plt.show()