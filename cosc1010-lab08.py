# Jared Vickrey
# UWYO COSC 1010
# 11/12/24
# Lab 08
# Lab Section:10
# Sources, people worked with, help given to: https://stackoverflow.com/a/65929692
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def checkFloat(i):
    try:
        float(i)
        return True
    except ValueError:
        return False
    
def checkInt(i):
    try:
        int(i)
        return True
    except ValueError:
        return False


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate

# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list


def slopeIntercept(m,b,xLower,xUpper):
    yValues = []
    for x in range(xLower, xUpper + 1):
        y = m * x + b
        yValues.append(y)
    return yValues

print('type "exit" to end')

while 1==1:
    m = input("Slope, m: ")
    if m.lower() == "exit":
        break
    if not checkFloat(m):
        print("Invalid input")
        continue
    m=float(m)
    b = input("X Intercept, B: ")
    if not checkFloat(b):
        print("Invalid input")
        continue
    b=float(b)
    xUpper = input("Upper bound for X: ")
    if not checkInt(xUpper):
        print("Invalid input")
        continue
    xUpper=int(xUpper)
    xLower = input("Lower bound for X: ")
    if not checkInt(xLower):
        print("Invalid input")
        continue
    xLower=int(xLower)
    if xLower > xUpper:
        print("Invalid input")
        continue
    print(slopeIntercept(m,b,xLower,xUpper))
    break

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
def checkSqrt(i):
    if i < 0:
        return None
    else:
        return i ** 0.5

def quadraticFormula(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    sqrtDisc = checkSqrt(discriminant)
    if sqrtDisc is None:
        return None
    x1 = (-b + sqrtDisc) / (2 * a)
    x2 = (-b - sqrtDisc) / (2 * a)
    return [x1, x2]

print('type "exit" to end')

while True:
    a = input("Coefficient a: ")
    if a.lower() == "exit":
        break
    if not checkFloat(a):
        print("Invalid input")
        continue
    a = float(a)
    if a == 0:
        print("Invalid input")
        continue
    b = input("Coefficient b: ")
    if not checkFloat(b):
        print("Invalid input")
        continue
    b = float(b)
    c = input("Coefficient c: ")
    if not checkFloat(c):
        print("Invalid input")
        continue
    c = float(c)
    result = quadraticFormula(a, b, c)
    if result is None:
        print("No real solutions")
    else:
        print("Solutions are:", result)
    break
