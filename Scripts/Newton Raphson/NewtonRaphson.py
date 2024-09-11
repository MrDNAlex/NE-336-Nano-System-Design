# Newton Raphson Method Formulation
def NewtonRaphson (x0, f, fp, tolerance = 0.005, maxIteration = 100):
    xold = x0
    xnew = 0
    count = 0
    error = 1000
    
    xHistory = []
    xHistory.append(x0)
    errorHistory = []
    
    while (error > tolerance and count < maxIteration):
        xnew = xold - f(xold)/fp(xold)
        error = abs((xnew - xold)/xnew)*100
        xHistory.append(xnew)
        errorHistory.append(error)
        count +=1
        xold = xnew    

    return (xHistory, errorHistory)

