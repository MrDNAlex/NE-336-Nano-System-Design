from scipy.optimize import fsolve

# Alexandre Dufresne-Nappert
# 20948586

# x^4+2xy^2=4
# x^3*y - 4y = 1



def func (var):
    
    # Unpack variables
    [x, y] = var
    
    EQ1 = x**4 + 2*x*y**2 - 4
    EQ2 = x**3*y-4*y-1
    
    return [EQ1, EQ2]

# Solve the function
solution = fsolve(func, (1.414, 0))


# Display the result
print(f"\nRoots are : x = {solution[0]} and y = {solution[1]}")

# Solve for the other root
solution2 = fsolve(func, (-1, -0.2))

# Display the other solution
print(f"\nRoots are : x = {solution2[0]} and y = {solution2[1]}")