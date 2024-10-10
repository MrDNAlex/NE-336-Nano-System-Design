import numpy as np

# Permutation Function, Generates all possible permutations
def Permuations (data, i, length, perms = []):
    if i ==length:
        perms.append(data.copy())
    else:
        for j in range(i, length):
            
            # Cache the Values
            dataI = data[i]
            dataJ = data[j]
            
            # Swap the Values
            data[j] = dataI
            data[i] = dataJ
            
            # Go through permutations one level deeper
            Permuations(data, i + 1, length, perms)
            
            # Swap Back
            data[i] = dataI
            data[j] = dataJ
    return perms


# Solves a Generic Matrix with Gauss Siedel, if it encouters division by Zero it returns None
def GaussSiedel (A, x, b, iter = 100):
    # Loop over Equations
    n = len(b)
    for k in range(iter):
        for i in range(n):
            
            if (A[i,i] == 0):
                return None
            
            sumTop = b[i]
            for j in range(n):
                if (i == j):
                    continue
                
                sumTop -= A[i, j]*x[j]
            
            x[i] = sumTop / A[i, i]
            
    return x

# Initialize Matrices and Problem
b = [247, 248, 239]
x = [10, 10, 10]       
A = [[0.2425, 0, -0.9701],
    [0, 0.2425, -0.9701],
    [-0.2357, -0.2357, -0.9428]]

n = len(b)

# Iterations
iter = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Loop through Iterations
for i in range(len(iter)):
    print("\n")
    print(f"Iterations : {iter[i]}")
    
    # Loop through Every Permutation, rebuild A, b and x and then solve using Gauss Siedel
    for perms in Permuations([0, 1, 2], 0, 3, []):
        
        # Remake A
        newA = np.zeros((n, n))
        for j in range(n):
            newA[j] = A[perms[j]]
            
        # Remake b
        newb = np.zeros(n)
        for j in range(n):
            newb[j] = b[perms[j]]
            
        # Remake x 
        newX = np.zeros(n)
        for j in range(n):
            newX[j] = x[perms[j]]
            
        Sol = GaussSiedel(newA, newX, newb, iter[i])
        
        if (Sol is None):
            continue
        
        print("\n")
        print(f"Permutation : {perms}")
        print(f"x1 : {Sol[0]}, x2 : {Sol[1]}, x3 : {Sol[2]}")
        print("\n")
    
    