#once you have completed your scheme.py file, include it in the same path as
#mybisection.py so that the following line 
from scheme import mypolyval
#would import the horner scheme solution function so we can use it in this file

#also import the bisection method from scipy for testing 
from scipy.optimize import bisect 

#import sign from numpy, we dont need any other function from it!
from numpy import sign

# Alexandre Dufresne-Nappert   20948586

#now for bisection
def bisection(polyf, xl, xu):
	'''
	(list,float,float)->float
	This function finds a root xroot for the function polyf
	between xl and xu using the bisection method.
	inputs : polyf function to find roots for
	xl lower bound of interval
	xu upper bound of interval
	output : xroot root of the function
	'''
 
	if (not isinstance(xl, (float, int))):
		print("xl is not a Number, input a number please")
		return None

	if (not isinstance(xu, (float, int))):
		print("xu is not a Number, input a number please")
		return None
 
	if (mypolyval(polyf,xl) == None or mypolyval(polyf, xu) == None):
		print("Not every value in the polynomial is a Number")
		return None

	xLow = xl
	xUp = xu
 
	yLower = mypolyval(polyf, xLow)
	yUpper = mypolyval(polyf, xUp)
 
	if (sign(yLower) == sign(yUpper)):
		print("The Bounds you've selected probably don't encapsulate a root")
		return None

	count = 0
	maxCount= 100
	error = 1000
	while (count < maxCount and error > 10**(-6)):
		xMid = (xLow + xUp)/2
		yLower = mypolyval(polyf, xLow)
		yMiddle = mypolyval(polyf, xMid)

		if (sign(yLower) != sign(yMiddle)):
			temp = xUp
			xUp = xMid
			error = abs(xUp - temp)/xUp
		else:
			temp = xLow
			xLow = xMid
			error = abs(xLow - temp)/xLow
   
		count += 1
    
	return xMid #remove this and start writing the function


if __name__=="__main__":
	#Test
	polyTest1 = [-6, "Hello", 4, 1]
	polyTest2 = [-6, 3, 4, 1]
	polyTest3 = [-6, 3, 4, 1]
	polyTest4 = [-6, 3, 4, 1]
 
	xlTest1 = 0
	xlTest2 = "Hello"
	xlTest3 = 0
	xlTest4 = 0
 
	xuTest1 = 5
	xuTest2 = 5
	xuTest3 = "Hello"
	xuTest4 = 5
 
	fTest = lambda x : x**3+4*x**2+3*x-6
 
	tests = [[polyTest1, xlTest1, xuTest1, fTest],[polyTest2, xlTest2, xuTest2, fTest],[polyTest3, xlTest3, xuTest3, fTest],[polyTest4, xlTest4, xuTest4, fTest]]
	
	for i in range(len(tests)):
		myBisect = bisection(tests[i][0], tests[i][1],tests[i][2])
  
		if (myBisect == None):
			print("Bisect Caught error successfully")
			continue

		scipyBisect = bisect(tests[i][3], tests[i][1], tests[i][2])
  
		print(myBisect)
		print(scipyBisect)
  
		if (abs(myBisect - scipyBisect) < 10**(-6)):
			print("Success")
	
	