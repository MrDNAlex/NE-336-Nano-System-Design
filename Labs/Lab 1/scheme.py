from numpy.polynomial import Polynomial

# Alexandre Dufresne-Nappert   20948586

def mypolyval(p,x):
    
    if (not isinstance(x, (float, int))):
        print("x is not a floating point number")
        return None
    
    if (not isinstance(p, list) or len(p) == 0):
        print("p is not a list, or is empty")
        return None
    
    if (not all([isinstance(i, (float, int)) for i in p])):
        print("Not every item in the list is a float")
        return None
    
    polysum = 0
    
    for i in range(len(p) -1 , 0, -1):
        polysum+= p[i]
        polysum*= x
        
    polysum += p[0]
    
    return polysum
    
if __name__=="__main__":
    
    # Evaluating
    polyTest1 = [4, "Hello", 2, 13, 20]
    polyTest2 = [4, 0, 2, 13, 20]
    polyTest3 = [4, 0, 2, 13, 20]
    
    xTest1 = 4
    xTest2 = "hello"
    xTest3 = 4
    
    tests = [[polyTest1, xTest1], [polyTest2, xTest2], [polyTest3, xTest3]]
    
    for i in range(len(tests)):
        myPoly = mypolyval(tests[i][0], tests[i][1])
        
        if (myPoly == None):
            print("mypolyval caught an error successfully")
            continue
        
        npPoly = Polynomial(tests[i][0])(tests[i][1])
        
        print(myPoly)
        print(npPoly)
        
        if (abs(myPoly - npPoly) < 10**(-5)):
            print("Success")
        
    
	#test your function here
	#you could start with testing it for 20x**4+13x**3-2x**2+4 = 5988