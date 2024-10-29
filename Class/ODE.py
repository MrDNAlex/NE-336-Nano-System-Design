import numpy as np

dxdt = lambda t: -2*t**3+12*t**2-20*t+8.5
xreal = lambda t : -0.5*t**4+4*t**3-10*t**2+8.5*t+1

# Euler
# xi +1 = xi + f(ti, xi)*dt

x0 = 1
(t0, tend)=(0, 4)
dt = 0.5

n = int((tend - t0)/dt+1)
t = np.linspace(t0, tend, n)

# True solution
x = np.zeros(n)
x[0] = x0

for i in range(1, n):
    x[i] = x[i-1] + dxdt(t[i-1])*dt

print(x)

i=1
while (i < n):
    x[i] = x[i-1] + dxdt(t[i-1])*dt
    i+=1

print(x)


#RK4 Method
dxdt = lambda t,x: 4*np.exp(0.8*t) - 0.5*x

(t0, tend)=(0, 4)
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
    
print(x)