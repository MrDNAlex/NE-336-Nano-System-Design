import numpy as np

def IsItSquare(A):
    '''
    (ndarray)-> None 
    >>>IsItSquare([[1,2,3],[4,5,6]]) 
    The function needs an array as input
    >>>IsItSquare(np.array([[1,2,3],[4,5,6]])) 
    The matrix is 2 by 3 and the determinant cannot be evaluated. 
    >>>IsItSquare(np.arange(1,10).reshape(3,3)) 
    The array is a square matrix with the det=-9.51619735392994e-16
    '''
    if (type(A) != np.ndarray):
        print("The function needs an array as input")
        return None
    
    shapeOfA = np.shape(A)
    
    if len(shapeOfA) != 2:
        print("Array is not 2 Dimensions")
        return None
    
    if (shapeOfA[0] != shapeOfA[1]):
        print(f"The Matrix is {shapeOfA[0]} by {shapeOfA[1]} and the determinant cannot be evaluated")
        return None
    
    print(f"The Array is a Square Matrix with the det={np.linalg.det(A)}")
    
    
IsItSquare([[1,2,3],[4,5,6]]) 
IsItSquare(np.array([[1,2,3],[4,5,6]])) 
IsItSquare(np.arange(1,10).reshape(3,3)) 