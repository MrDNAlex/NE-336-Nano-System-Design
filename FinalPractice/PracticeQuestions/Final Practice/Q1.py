from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np

def DMdt (t, A):
    
    # Unpack the variables
    [M, S] = A
    
    EQ1 = 10
    EQ2 = 10*0.2 - 10*(S/M)
    
    return [EQ1, EQ2]



# Define intial Values 
MInit = 1000
SInit = 200

init = [MInit,SInit]

T0 = 0
TEnd = 120

tVals = np.linspace(T0, TEnd, 1000)

solution = solve_ivp(DMdt,(T0, TEnd), init, t_eval=tVals)

M = solution.y[0]
S = solution.y[1]

fig, ax1 = plt.subplots()

ax1.plot(tVals, M, label="M")
ax1.twinx().plot(tVals, S, label="S")

plt.legend()
plt.show()

plt.figure(figsize=(16, 10))
plt.plot(tVals, S/M, label="S/M")
plt.legend()
plt.show()