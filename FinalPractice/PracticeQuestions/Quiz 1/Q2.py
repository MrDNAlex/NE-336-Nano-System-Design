import numpy as np



def is_diag_dominant (A):
    
    
    if not isinstance(A, np.ndarray):
        print("Inputted value should be an Array or Matrix")
        return None
    
    shape = A.shape
    
    if len(shape) != 2 or shape[0] != shape[1]:
        print("Matrix is not Square")
        return None
    
    
    diagonalElements = np.abs(np.diag(A))
    
    rowSums = np.sum(A, axis=1) - diagonalElements
    
    if np.all(rowSums < diagonalElements):
        print("Diagonally Dominant")
        return True
    
    else:
        print("Not Diagonally Dominant")
        return False


if __name__ == "__main__":
    
    A = np.array([[2, -6, -1], [-3, -1, 7], [-8, 1, -2]])
    
    b = np.array([-38, -34, -20])

    is_diag_dominant([1, 2, 3])
    
    is_diag_dominant(A)
    
    A = np.array([[-8, 1, -2], [2, -6, -1], [-3, -1, 7]])
    
    b = np.array([-20, -38, -34])
    
    is_diag_dominant(A)
    
    # No the system would not converge using Gauss Siedel method if the system was not diagonally dominant.
    # To Ensure stability and convergence the system must diagonally dominant when using the Gauss seidel method

    x1 = 1
    x2 = 1
    x3 = 1

    tol = 10**-5
    
    for i in range(10):
        
        newx1 = (b[0] - A[0, 1]*x2 - A[0, 2]*x3)/A[0, 0]
        e1 = abs(newx1 - x1)/newx1
        x1 = newx1
        
        newx2 = (b[1] - A[1, 0]*x1 - A[1, 2]*x3)/A[1, 1]
        e2 = abs(newx2 - x2)/newx2
        x2 = newx2
         
        newx3 = (b[2] - A[2, 0]*x1 - A[2, 1]*x2)/A[2, 2]
        e3 = abs(newx3 - x3)/newx3
        x3 = newx3
        
        print(f"X1 = {x1}")
        print(f"X2 = {x2}")
        print(f"X3 = {x3}")
        
        if (e1 < tol and e2 < tol and e3 < tol):
            print(e1, e2, e3)
            print("Converged")
            break
        
    
    print("Done")