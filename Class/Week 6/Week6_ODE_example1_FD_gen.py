import numpy as np
import matplotlib.pyplot as plt

#constants from the question
T0 = 40
Tend = 200
Ta = 20
L = 10
h = 0.01

#number of total nodes
n=6

#dx
dx=L/(n-1)

#initialize T
T=np.zeros(n)
#apply BCs
T[0]=T0
T[-1]=Tend

#making the A matrix

#2+hdx**2 on diag
#-1 on off diag
A=np.diag((2+h*dx**2)*np.ones(n-2))+np.diag(-1*np.ones(n-3),1)+\
  np.diag(-1*np.ones(n-3),-1)

#lets check A
print(A)

#making b !
#h dx**2 Ta in all terms
#b[0] has +T0
#b[-1] has +Tend
b= h*dx**2*Ta*np.ones(n-2)
b[0]+=T0
b[-1]+=Tend


#now solve!
T[1:-1]=np.linalg.solve(A,b)

print(T)

#from last week!
#solve for c1 c2 for analytical solution
A = np.array([[1,1],[2.718,0.368]])
b = np.array([T0-Ta,Tend-Ta])
c = np.linalg.solve(A,b)

#added in the analytical solution
T_analytical=lambda x : c[0]*np.exp(0.1*x)+c[1]*np.exp(-0.1*x)+Ta

xvals=np.linspace(0,L,n)
plt.figure()
plt.plot(xvals,T_analytical(xvals),'b-',label='analytical')
plt.plot(xvals,T,'ro',label='FD')
plt.legend()
plt.xlabel('x')
plt.ylabel('T')
plt.show()