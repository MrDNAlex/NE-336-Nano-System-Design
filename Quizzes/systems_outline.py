import numpy as np 

def is_diag_dominant(A):
    #check conditions for returning None. 
	
    #check A is array
    if type(A)!= np.ndarray:
        return None
		
    #get the shape tuple 
    A_shape=A.shape
	
	
    #this statement first checks that A is 2d and square 
    if len(A_shape)!=2 or A_shape[0]!=A_shape[1]:
        return None 
	
	
    #find abs value of diagonal coefficients 
    diag_elements=np.abs(np.diag(A))


    #find row sum without diagonal
    off_diagonal_sum = np.sum(np.abs(A),axis=1)-diag_elements
	


    #compare these values to see if diagonally dominant
    #use all to check all values are greater on diag 
    if np.all(off_diagonal_sum < diag_elements):
        print("It is diagonally dominant. ")
        return True
    else:
        print("It is NOT diagonally dominant.")
        return False 
    
    
    
    
if __name__=="__main__":
    
    # 3.2.1
    result1 = is_diag_dominant([1, 2, 3])
    print(result1)
    
    
    #3.2.2
    A = np.array([[2, -6, -1], [-3, -1, 7], [-8, 1, -2]])
    b = np.array([ [-38], [-34], [-20]])
    
    print(A)
    print(b)
    
    #3.2.3
    
    result2 = is_diag_dominant(A)
    # Not dominant so we need to rearrange
    # New A matrix is as follows
    A = np.array([[-8, 1, -2],  [2, -6, -1], [-3, -1, 7] ])
    b = np.array([[-20], [-38], [-34]])
    
    if ( is_diag_dominant(A)):
        print("We Are Now Diagonally Dominant")
        
    
    #3.2.4
    # Gauss Siedel would not converge properly if we are not diagonally dominant
    
    #3.2.5
    tol = 10**(-5)
    x1 = 1
    x2 = 1
    x3 = 1
    
    for i in range(10):
        x1n = (b[0] - A[0, 1]*x2 - A[0, 2]*x3) / A[0, 0]
        e1 = abs(x1n - x1)/x1n
        x1 = x1n
        
        x2n = (b[1] - A[1, 0]*x1 - A[1, 2]*x3) / A[1, 1]
        e2 = abs(x2n - x2)/x2n
        x2 = x2n
        
        x3n = (b[2] - A[2, 1]*x2 - A[2, 0]*x1) / A[2, 2]
        e3 = abs(x3n - x3)/x3n
        x3 = x3n
        print(e1, e2, e3)
        
        if (e1 < tol and e2 < tol and e1 < tol):
            print(e1, e2, e3)
            print("Converged")
            break
        
        
    print(x1, x2, x3)

    #answer quiz here