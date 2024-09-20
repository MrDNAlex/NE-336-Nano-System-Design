# Summation Function Definition
def summationV1 (x):
    
    if (not isinstance(x, (int, float))):
        print(f"X is not a Number (x = {x})")
        return None

    if (abs(x) >= 1):
        print(f"X's Value is larger than or equal to 1. X must be smaller than 1 (x = {x})") 
        return None
        
    sum = 0
    n = 0
    maxLoops = 100
    while n < maxLoops:
        exponent = 2 * n + 1
        value = x**(exponent)
        
        if abs(value) < 10**(-5):
            return sum
        
        sum += value
        n += 1
        
# Summation V2 (With Custom tolerance) Function Definition
def summationV2 (x, tolerance = 10**(-5)):

    if (not isinstance(x, (int, float))):
        print(f"X is not a Number (x = {x})")
        return None
    
    if (not isinstance(tolerance, (int, float))):
        print(f"Tolerance is not a Number (tolerance = {tolerance})")
        return None

    if (abs(x) >= 1):
        print(f"X's Value is larger than or equal to 1. X must be smaller than 1 (x = {x})") 
        return None
        
    sum = 0
    n = 0
    maxLoops = 100
    while n < maxLoops:
        exponent = 2 * n + 1
        value = x**(exponent)
    
        if abs(value) < tolerance:
            return sum
        
        sum += value
        n = n + 1

# True function representing the Value
def trueEquation (x):
    return (x/(1 - x**2))
