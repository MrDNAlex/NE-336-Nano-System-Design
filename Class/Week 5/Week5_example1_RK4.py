#example 1 shooting method
import numpy as np
import matplotlib.pyplot as plt

# =================== #
# Define parameters   #
# =================== #
# here, we define all the parameters at the top of 
#the file and use them below

Tinf=20 #deg C
T_x0=40 #deg C
T_end=200 #deg C
hp=0.01#/m2

def dfdx(x,f):
    #even though the indep var x isnt here, its important to include it (we will see why later)
    #f is the vector [T,u]
    #where u is dTdx
    #so dfdx is [u,h'(T-Tinf)]
	
    dfdx_vals=[0,0]
    dfdx_vals[0]=f[1] #this is u
    dfdx_vals[1]=hp*(f[0]-Tinf)
	
    return np.array(dfdx_vals)

def rk4(df,xval,IC):
    #I have decided to write a function for this to make it easier to call
    #df is the system of DEs
    #xvals are the values for the indep var to integrate at 
    #IC should be a vector of the ICs 
    f_vals=np.zeros((xval.size,2))
    f_vals[0,:]=IC
	
    delx=xval[1]-xval[0]#find dx from xvals!
	
    for i in range(1,xval.size):
        k1=df(xval[i-1],f_vals[i-1,:])
        k2=df(xval[i-1]+delx/2,f_vals[i-1,:]+k1*delx/2)
        k3=df(xval[i-1]+delx/2,f_vals[i-1,:]+k2*delx/2)
        k4=df(xval[i-1]+delx,f_vals[i-1,:]+k3*delx)
        phi=(k1+2*k2+2*k3+k4)/6
        f_vals[i,:]=f_vals[i-1,:]+phi*delx
	
    return f_vals
	
	
#solve for c1 c2 for analytical solution
A = np.array([[1,1],[np.exp(1),np.exp(-1)]])
b = np.array([T_x0-Tinf,T_end-Tinf])
c = np.linalg.solve(A,b)

#added in the analytical solution
T_analytical=lambda x : c[0]*np.exp(0.1*x)+c[1]*np.exp(-0.1*x)+Tinf

#lets use RK4
#values needed for integration
dx=2 
(x0,xend)=(0,10)
n=int((xend-x0)/dx + 1) #number of points
x_val=np.linspace(x0,xend,n)


#shooting method    
#first guess at u
u_guess1=10
T_rk_guess1 = rk4(dfdx,x_val,[T_x0,u_guess1])

#lets check if the T(x=10) matches our BC?
print("with a first guess of dTdx(x=0) =",u_guess1,end=' ')
print("the temperature at  x=",xend,"is",T_rk_guess1[-1,0],"and should be",T_end)

#second guess at u
u_guess2=20
T_rk_guess2 = rk4(dfdx,x_val,[T_x0,u_guess2])

#lets check if the T(x=10) matches our BC?
print("with a second guess of dTdx(x=0) =",u_guess2,end=' ')
print("the temperature at  x=",xend,"is",T_rk_guess2[-1,0],"and should be",T_end)

#third guess, interpolate or extrapolate!
#in this case interpolate
#p1(x)=b0+b1(x-x0)
#b1 is the slope of the line 
b1=(T_rk_guess1[-1,0]-T_rk_guess2[-1,0])/(u_guess1-u_guess2)
b0= T_rk_guess1[-1,0]

#we want the x for which
#p1(x)=T(x=10)=b0+b1(x-x0)
u_guess3=(T_end-b0)/b1+u_guess1

#third (and hopefully final!) guess at u
T_rk_guess3 = rk4(dfdx,x_val,[T_x0,u_guess3])

#lets check if the T(x=10) matches our BC?
print("with a third guess of dTdx(x=0) =",u_guess3,end=' ')
print("the temperature at  x=",xend,"is",T_rk_guess3[-1,0],"and should be",T_end)


#now lets plot the results against each other 
plt.figure()
plt.subplot(221)
plt.plot(x_val,T_analytical(x_val),'-k',label='analytical')
plt.plot(x_val,T_rk_guess1[:,0],'ro',label='values from u0='+str(u_guess1))
plt.legend()
plt.xlabel('x')
plt.ylabel('T(x)')

plt.subplot(222)
plt.plot(x_val,T_analytical(x_val),'-k',label='analytical')
plt.plot(x_val,T_rk_guess2[:,0],'bo',label='values from u0='+str(u_guess2))
plt.legend()
plt.xlabel('x')
plt.ylabel('T(x)')

plt.subplot(212)
plt.plot(x_val,T_analytical(x_val),'-k',label='analytical')
plt.plot(x_val,T_rk_guess3[:,0],'go',label='values from u0='+str(round(u_guess3,4)))
plt.legend()
plt.xlabel('x')
plt.ylabel('T(x)')
plt.show()