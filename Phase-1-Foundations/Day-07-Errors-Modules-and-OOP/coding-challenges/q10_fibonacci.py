"""
Problem 10 - Fibonacci sequence   (Day 4: loops & the swap trick)   [STUB]

Return a list of the first `count` Fibonacci numbers. Each number is the sum of
the previous two, starting 0, 1.
Example: count = 10 -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Skills: loop, list accumulator, updating two variables at once (a, b = b, a + b).

Run:
    python q10_fibonacci.py
"""

def fibonacci(count):
    """Return a list of the first `count` Fibonacci numbers."""
    # TODO: start a, b = 0, 1  and an empty list `seq`
    # TODO: loop `count` times: append a, then update a, b = b, a + b
    # TODO: return seq
    pass


if __name__ == "__main__":
    print(fibonacci(10))   # expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    print(fibonacci(1))    # expected: [0]
