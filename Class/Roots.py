import numpy as np
import matplotlib.pyplot as plt

f = lambda x:x*np.log(x) - x

x = np.linspace(1, 6)

xu = 6
xl = 1

fxu = f(xu)
fxl = f(xl)

x = np.linspace(xl, xu, 500)

maxIter = 500-1
count = 0
while (count < maxIter):
    xold = x[count]
    xnew = x[count + 1]
    
    if f(xold)*f(xnew)< 0:
        print("Range is : " + str((xold, xnew)))
        break
    
    count+= 1