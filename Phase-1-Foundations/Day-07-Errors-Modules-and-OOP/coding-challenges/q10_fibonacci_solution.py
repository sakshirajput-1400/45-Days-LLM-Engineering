"""
Problem 10 - Fibonacci sequence   (SOLUTION)

Run:
    python q10_fibonacci_solution.py

Logic note:
  a, b = b, a + b updates BOTH variables at once using the old values on the
  right-hand side. Doing it in two separate lines would overwrite `a` before you
  could use it -- the simultaneous assignment is what makes it clean.
"""

def fibonacci(count):
    """Return a list of the first `count` Fibonacci numbers."""
    seq = []
    a, b = 0, 1
    for _ in range(count):
        seq.append(a)
        a, b = b, a + b      # advance the pair in one step
    return seq


if __name__ == "__main__":
    print("first 10 :", fibonacci(10))
    print("first 1  :", fibonacci(1))
    print("first 0  :", fibonacci(0))
