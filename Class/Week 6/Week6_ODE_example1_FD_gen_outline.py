import numpy as np

#constants from the question
T0 = 40
Tend = 200
Ta = 20
L = 10
h = 0.01

#number of total nodes
n = 6

#dx
dx = L/(n-1)

#initialize T
T = np.zeros(n)

#apply BCs
T[0] = T0
T[n-1] = Tend
print(T)

#now make A!
#2+hdx**2 on diag
#-1 on off diag



#make b!
#h dx**2 Ta in all terms
#b0 has +T0
#bend has +Tend



#now solve for T
