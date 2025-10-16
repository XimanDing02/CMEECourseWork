# This is only the ocde file.
# All my understanding of these code below are shown in my week2 readme file. 
# cfexercises1.py
#!/usr/bin/env python3

"""Some functions exemplifying the use of control statements"""
#docstrings are considered part of the running code (normal comments are
#stripped). Hence, you can access your docstrings at run time.
__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.1'

def foo_1(x):
    return x ** 0.5

def foo_2(x, y):
    if x > y:
        return x
    return y

def foo_3(x, y, z):
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return [x, y, z]

def foo_4(x):
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

def foo_5(x): # a recursive function that calculates the factorial of x
    if x ==0 or x == 1:
        return 1
    return x * foo_5(x - 1)
     
def foo_6(x): # Calculate the factorial of x in a different way; no if statement involved
    facto = 1
    if x == 0:
        return 1
    while x >= 1:
        facto = facto * x
        x = x - 1
    return facto

# like the program-with-control-flows example in the book, in the book they copy and rename boilerplate.py to control_flow.py
# here I will use the same way to test my functions in lc1.py
if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer n for tests (e.g., 5): "))
        if n < 0:
            raise ValueError("n must be non-negative")
    except Exception as e:
        print(f"[Input error] {e}. Using default n = 5")
        n = 5

    print(f"foo_1({n}) =", foo_1(n))
    print(f"foo_2({n}, 7) =", foo_2(n, 7))
    print(f"foo_3({n}, 2, 9) =", foo_3(n, 2, 9))
    print(f"foo_4({n}) =", foo_4(n))
    print(f"foo_5({n}) =", foo_5(n))
    print(f"foo_6({n}) =", foo_6(n))
        # Additional tests
    print("\n[Extra tests]")
    print("foo_5(10) =", foo_5(10))
    print("foo_6(10) =", foo_6(10))
