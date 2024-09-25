import numpy as np

# This is functional
def RK4 (dxdt, t0, tend, x0) :

    x0 = 2
    dt = 1

    n =  int((tend - t0)/dt+1)

    t = np.linspace(t0, tend, n)
    x = np.zeros(n)
    x[0] = x0

    for i in range(1, n):
        k1 = dxdt(t[i-1], x[i-1])
        k2 = dxdt(t[i-1]+0.5*dt, x[i-1]+0.5*k1*dt)
        k3 = dxdt(t[i-1]+0.5*dt, x[i-1]+0.5*k2*dt)
        k4 = dxdt(t[i-1]+dt, x[i-1]+k3*dt)
        
        phi = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        
        x[i] = x[i - 1] + phi
        
    return x