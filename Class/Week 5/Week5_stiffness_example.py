import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

dxdt_fun = lambda t,x: x**2 *(1-x)


x0=[1e-4,1e-5,1e-6]


for x0_val in x0:
    plt.figure()
    sol=solve_ivp(dxdt_fun,[0,2/x0_val],[x0_val])
    plt.plot(sol.t,sol.y.ravel(),'ro',mfc='w',label='soln with x0='+str(x0_val))
    plt.legend()
    plt.show()


#how make this better? change method!