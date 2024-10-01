#is this correct?
from scipy.integrate import solve_ivp


#fix mistake 
dxdt = lambda x: x**2*(1-x)


x0=1e-4
sol= solve_ivp(dxdt,[0,2/x0],[x0])

#how to evaluate this for two other x0 values?