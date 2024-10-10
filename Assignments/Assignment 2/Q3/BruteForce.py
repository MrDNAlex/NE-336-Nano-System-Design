import numpy as np


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
      
b = [247, 248, 239]
x = [10, 10, 10]       
A = [[0.2425, 0, -0.9701],
    [0, 0.2425, -0.9701],
    [-0.2357, -0.2357, -0.9428]]

n = len(b)

#Loop through all the Permutations
for perms in Permuations([0, 1, 2], 0, 3):
    
    # Remake A
    newA = np.zeros((n, n))
    for i in range(n):
        newA[i] = A[perms[i]]
        
    # Remake b
    newb = np.zeros(n)
    for i in range(n):
        newb[i] = b[perms[i]]
        
    # Remake x 
    newX = np.zeros(n)
    for i in range(n):
        newX[i] = x[perms[i]]
        
    Sol = GaussSiedel(newA, newX, newb)
    
    print(Sol)
        
        
        
    
        
    
    
    
    

        
        
    
    
    
    
    
    