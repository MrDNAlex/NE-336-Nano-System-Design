import numpy as np
import matplotlib.pyplot as plt

#constants from the question
m = 50
T0 = 40
Tend = 200
Ta = 20
L = 10
h = 0.01

#DX
dx = L/(m-1)

#Initialize T
T = np.zeros(m)
T[0] = T0
T[-1] = Tend

#Setup A Matrix
A = np.diag((2+h*dx**2)*np.ones(m-2)) + np.diag(-1*np.ones(m-3),1) + np.diag(-1*np.ones(m-3),-1)

A[0, 1] = -2

# Make the b vector
b = np.ones(m-2)*Ta*h*dx**2
#b[0] += T0
b[-1] += Tend

T[1:-1] = np.linalg.solve(A,b)
print(T)


plt.plot(np.linspace(0,L,m),T, 'o-')
plt.show()