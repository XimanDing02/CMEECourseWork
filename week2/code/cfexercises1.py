# cfexercises1.py
from typing import List

def foo_1(x: float) -> float:
    """Return the square root of x (x ** 0.5)."""
    return x ** 0.5


def foo_2(x: float, y: float) -> float:
    """Return the larger of x and y without using max()."""
    if x > y:
        return x
    return y


def foo_3(x: float, y: float, z: float) -> List[float]:
    """Return [x, y, z] in ascending order using in-place swaps."""
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    return [x, y, z]


def foo_4(n: int) -> int:
    """Return n! via for-loop (iterative). n must be >= 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def foo_5(n: int) -> int:
    """Return n! via recursion. Handles n == 0. n must be >= 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:          # base case handles 0 and 1
        return 1
    return n * foo_5(n - 1)


def foo_6(n: int) -> int:
    """Return n! via while-loop. Handles n == 0. n must be >= 0."""
    if n < 0:
        raise ValueError("n must be >= 0")
    facto = 1
    while n >= 1:
        facto *= n
        n -= 1
    return facto


#if __name__ == "__main__":
    print("foo_1(9) ->", foo_1(9))
    print("foo_2(3, 5) ->", foo_2(3, 5))
    print("foo_3(9, 1, 5) ->", foo_3(9, 1, 5))
    print("foo_4(5) ->", foo_4(5))
    print("foo_5(5) ->", foo_5(5))
    print("foo_6(5) ->", foo_6(5))
