from numpy.polynomial import Polynomial

def mypolyval(p,x):
    
    if (not isinstance(x, (float, int))):
        print("x is not a floating point number")
        return None
    
    if (not isinstance(p, list)):
        print("p is not a list")
        return None
    
    if (not all([isinstance(i, (float, int)) for i in p])):
        print("Not every time in the list is a float")
        return None
    
    polysum = 0
    
    for i in range(len(p) -1 , 0, -1):
        polysum+= p[i]
        polysum*= x
        
    polysum += p[0]
    print(polysum)
    
if __name__=="__main__":
    
    # Evaluating
    
    
    
    mypolyval([4, 0, 2, 13, 20], "Hello")
    mypolyval([4, "hello", 2, 13, 20], 4)
    mypolyval([4, 0, 2, 13, 20], 4)
    
    poly = Polynomial([4, 0, 2, 13, 20])
    
    print(poly(4))
    
	#test your function here
	#you could start with testing it for 20x**4+13x**3-2x**2+4 = 5988