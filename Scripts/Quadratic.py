import numpy

def quadratic_root(a ,b ,c):
    
    """
    (float, float, float) -> tuple
    
    Return the roots of a quadratic function f(x) = a x^2 + b x + c with real coefficients.
    
        >>> quadratic_root(-1., 2., 3.)
        (3.0,-1.0)
        >>> quadratic_root(1, 0., -4.)
        (2.0,-2.0)

    """
    delt=(b*b)-4*a*c
    
    x1,x2= ((-b+numpy.sqrt(delt))/(2*a),  (-b-numpy.sqrt(delt))/(2*a))
   
    # using the quadratic formula, compute the two roots of the polynomial
    
    return (x1,x2)

if __name__ == "__main__":
    (a, b, c) = (-1., 2., 3.)
    (x1, x2) = quadratic_root(a ,b ,c)
    print(f" X1 : {x1}, X2 : {x2}")