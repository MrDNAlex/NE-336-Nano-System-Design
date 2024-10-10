# Newton Raphson Method Formulation
def NewtonRaphson (x0, f, fp = None, tolerance = 0.005, maxIteration = 100):
    xold = x0
    xnew = 0
    count = 0
    error = 1000
    delta = 10**(-6)
    
    xHistory = []
    xHistory.append(x0)
    errorHistory = []
    
    while (error > tolerance and count < maxIteration):
        
        fpVal = 1
        
        if (fp is None):
            fpVal = (f(xold + delta) - f(xold)) / delta
        else:
            fpVal = fp(xold)
        
        
        xnew = xold - f(xold)/fpVal
        error = abs((xnew - xold)/xnew)*100
        xHistory.append(xnew)
        errorHistory.append(error)
        count +=1
        xold = xnew    

    return (xHistory, errorHistory)

