# This is only the code file.
# All my understanding of these code below are shown in my week2 readme file. 
# cfexercises1.py

def foo_1(x):
    # given by the question
    return x ** 0.5

def foo_2(x, y):
    # given by the question
    if x > y:
        return x
    return y

def foo_3(x, y, z):
    # given by the question
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return [x, y, z]

def foo_4(x):
    # given by the question
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo_5(x): # a recursive function that calculates the factorial of x
    # It seperately handles the base case when x is 0 or 1, returning 1 in those cases.
    if x == 0 or x == 1:
        return 1
    return x * foo_5(x - 1)
     
def foo_6(x): # Calculate the factorial of x in a different way; no if statement involved
    #  # It seperately handles the base case when x is 0 or 1, returning 1 in those cases.
    facto = 1
    if x == 0:
        return 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto
