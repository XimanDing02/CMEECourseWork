#MyExampleScript.py
def foo(x):
    """Print x squared (side effect)."""
    x *= x  # same as x = x * x
    print(x)

if __name__ == "__main__":
    foo(2)
