import numpy as np 
import matplotlib.pyplot as plt
from Week7_PDE_example1_complete import T

#nodes in x direction
m=3

#nodes in y dir 
n=3

print("The temperature distribution within the plate is:")
for i in range(1,n+1):
	print(T[i,1:m+1])


#example 2
qx=np.zeros(T.shape)
qy=np.zeros(T.shape)
k=0.49

delx=40/(m+1)
dely=40/(n+1)

for col in range(1,n+1):
    for row in range(1,m+1):
        qx[row,col]=-k*(T[row,col+1]-T[row,col-1])/(2*delx)
        qy[row,col]=-k*(T[row-1,col]-T[row+1,col])/(2*dely)       


qx=qx[1:m+1,1:n+1]
qy=qy[1:m+1,1:n+1]


qn=np.sqrt(qx**2+qy**2)

angles=np.arctan(qy/qx)*180/np.pi

#np.where can take a condition to find indices
#then apply first value to those
#and return second value to others
#try a=np.arange(10)
#np.where(a<5,-1,a)
angles_corrected= np.where(qx<0,angles+180,angles)

#plt.figure()
x,y=np.meshgrid(np.arange(1,m+1),np.arange(n,0,-1))
plt.quiver(x,y,qx,qy,angles='xy', scale_units='xy', scale=2)
plt.xlim(0.5,3.5)
plt.ylim(0,3)
plt.show()