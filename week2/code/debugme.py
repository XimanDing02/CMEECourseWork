#!/usr/bin/env python3
"""A debugging example script that demonstrates specific exception handling."""

__appname__ = 'debugme.py'
__author__ = 'Ximan Ding (x.ding25@imperial.ac.uk)'
__version__ = '0.0.3'
__license__ = "License for this code/program"

def buggyfunc(x):
    """Demonstrates try/except/else blocks with specific error handling."""
    y = x
    for i in range(x):
        try:
            y = y - 1
            z = x / y
        except ZeroDivisionError:
            print("The result of dividing a number by zero is undefined")
        except Exception:
            print(f"This didn't work; {x = }; {y = }")
        else:
            print(f"OK; {x = }; {y = }, {z = }")
    return z

def main():
    """Main entry point."""
    result = buggyfunc(20)
    print(f"\nFinal result: {result}")
    return 0

if __name__ == "__main__":
    main()