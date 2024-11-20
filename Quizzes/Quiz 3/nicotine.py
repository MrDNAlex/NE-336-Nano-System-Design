import numpy as np
import matplotlib.pyplot as plt

#spacing for x
dx=0.125
(x0,xend)=(0,2)
number_of_x=int((xend-x0)/dx + 1) #number of points in x
x_val=np.linspace(x0,xend,number_of_x)


#spacing for t
dt=0.05
(t0,tend)=(0,24)
number_of_t=int((tend-t0)/dt + 1) #number of points in t
t_val=np.linspace(t0,tend,number_of_t)


#values for k to test 
#k goes from 0 to 1 maximum 
number_of_k=11
k_vals=np.linspace(0,1,number_of_k)

#lambda=D delt/delx^2
D=0.1# cm^2 /s
lam=D*dt/dx**2

print(lam)


#we need as many rows as t, as many columns as x
#we can store each sol for new val of k in thrid dimension!
rho=np.zeros((number_of_t,number_of_x,number_of_k))

#IC
#rho=0
#rho[0,1:-1,:]=0


#BCs
#col 1 holds values at the patch
rho[:,0,:]=1


for j in range(number_of_k):
	for l in range(1,number_of_t-1):
		for i in range(1,number_of_x):
			if i==number_of_x-1:
				rho[l+1,i,j]=rho[l,i,j]+lam*(-2*rho[l,i,j]+2*rho[l,i-1,j])-k_vals[j]*dt*rho[l,i,j]
			else:
				rho[l+1,i,j]=rho[l,i,j]+lam*(rho[l,i+1,j]-2*rho[l,i,j]+rho[l,i-1,j])-k_vals[j]*dt*rho[l,i,j]
			



#snapshotplot for various k
snap1=100
snap2,snap3=2*snap1,3*snap1

for j in range(0,number_of_k,2):
	
	plt.figure()
	plt.plot(x_val,rho[snap1,:,j])
	plt.plot(x_val,rho[snap2,:,j])
	plt.plot(x_val,rho[snap3,:,j])
	plt.xlabel("x")
	plt.ylabel(r"$\rho$")
	plt.title(f"concentration as a function of x for k={k_vals[j]:.2f}")

	plt.legend(['t = '+str(t_val[snap1]) + ' h',\
				   't = '+str(t_val[snap2]) + ' h','t = '+str(t_val[snap3])+ ' h'])
		
		
#plots as function of time 
for j in range(0,number_of_k,2):
	plt.figure()
	plt.plot(t_val,rho[:,0,j],label='node = 0 (skin)')
	plt.plot(t_val,rho[:,number_of_x//8,j],label=f'node = {number_of_x//8}')
	plt.plot(t_val,rho[:,number_of_x//4,j],label=f'node = {number_of_x//4}')
	plt.plot(t_val,rho[:,number_of_x//2,j],label=f'node = {number_of_x//2}')
	plt.plot(t_val,rho[:,-1,j],label=f'node = {number_of_x-1} (bone)')
	plt.legend()
	plt.xlabel("t")
	plt.ylabel(r"$\rho$")
	plt.title(f"concentration as a function of x for k={k_vals[j]:.2f}")


