#!/usr/bin/env python3
"""
Auther: Ximan Ding (x.ding25@imperial.ac.uk)
Script: scope.py
Des: Exemplify use of global and local variables
Usage: python3 scope.py (in terminal)
Date: Oct, 2025
"""

# 1
# Define some global variables
_a_global = 10  # a global variable

if _a_global >= 5:
    _b_global = _a_global + 5  # also a global variable

print("Before calling a_function, outside the function, the value of _a_global is", _a_global)
print("Before calling a_function, outside the function, the value of _b_global is", _b_global)


def a_function():
    # Define local variables inside the function
    _a_global = 4  # this shadows the global variable
    if _a_global >= 4:
        _b_global = _a_global + 5  # local variable (not the same as global one)
    _a_local = 3

    # Print variables inside the function
    print("Inside the function, the value of _a_global is", _a_global)
    print("Inside the function, the value of _b_global is", _b_global)
    print("Inside the function, the value of _a_local is", _a_local)


# Call the function
a_function()

# Print variables outside the function again
print("After calling a_function, outside the function, the value of _a_global is (still)", _a_global)
print("After calling a_function, outside the function, the value of _b_global is (still)", _b_global)

# Remove the line that caused the NameError
# _a_local is not defined outside the function, so we skip printing it
print("Note: '_a_local' is a local variable inside the function and cannot be accessed here.")

# 2
# Demonstration of global vs local variable scope
# A global variable
_a_global = 10  

def a_function():
    # A local variable
    _a_local = 4  
    
    print("Inside the function:")
    print("  The value of _a_local is", _a_local)
    print("  The value of _a_global is", _a_global)  # accessible inside function

# Call the function
a_function()

# Outside the function
print("Outside the function:")
print("  The value of _a_global is", _a_global)

# Note:
# _a_global was available inside the function because it's defined globally.
# _a_local exists only within the function — it cannot be accessed outside.

# 3
# Demonstration: modifying a global variable inside a function using 'global'
# Define a global variable
_a_global = 10

print("Before calling a_function, outside the function, the value of _a_global is", _a_global)

def a_function():
    # Declare that we intend to use and modify the global variable _a_global
    global _a_global  
    
    # Modify the global variable
    _a_global = 5

    # Define a local variable (visible only inside this function)
    _a_local = 4
    
    # Print variable values inside the function
    print("Inside the function:")
    print("  The value of _a_global is", _a_global)
    print("  The value of _a_local is", _a_local)

# Call the function
a_function()

# Print the global variable again outside the function
print("After calling a_function, outside the function, the value of _a_global now is", _a_global)

# Explanation:
# Using the 'global' keyword made _a_global inside the function truly global.
# The assignment inside a_function() overwrote the original _a_global value (10 -> 5).

# 4
# Demonstration of global keyword in nested functions
# global inside nested function (local variable)
def a_function():
    _a_global = 10

    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling _a_function2, value of _a_global is", _a_global)
    
    _a_function2()
    
    print("After calling _a_function2, value of _a_global is", _a_global)

a_function()

print("The value of _a_global in main workspace / namespace now is", _a_global)

# 5
# global applied to existing global variable
_a_global = 10

def a_function():
    def _a_function2():
        global _a_global
        _a_global = 20
    
    print("Before calling a_function2, value of _a_global is", _a_global)
    _a_function2()
    print("After calling a_function2, value of _a_global is", _a_global)

a_function()

print("The value of a_global in main workspace / namespace is", _a_global)