

#lets import the Polynomial class for brevity 
from numpy.polynomial import Polynomial

#note that the coefficients in the series go from degree zero upwards
#so coeff[i] is for the term of degree i
#ax^2+bx+c is [c,b,a]

a=1
b=-1
c=-2
#creating polynomial 

#create polynomial from coefficients 
poly_1 = Polynomial([c,b,a])

#create polynomial from roots
poly_2 = Polynomial.fromroots([-1,2])

#are they the same?
print(poly_1==poly_2)

#find the roots of the first one
roots_poly_1=poly_1.roots()

print(f"the roots of {poly_1} are {roots_poly_1}")#formatted string print!

#evaluating a polynomial object is easy!
x=0
print(f"the the value of {poly_1} at x={x} is {poly_1(x)}")