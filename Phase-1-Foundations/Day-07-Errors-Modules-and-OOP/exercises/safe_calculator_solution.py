"""
Exercise 1 — Safe Calculator (solution).

Run (asks for input):
    python safe_calculator_solution.py
"""

class UnknownOperatorError(Exception):
    """Raised when the operator isn't one of + - * /."""

def calculate(a, b, op):
    """Return a op b, raising on a bad operator or divide-by-zero."""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b               # may raise ZeroDivisionError
    else:
        raise UnknownOperatorError(f"'{op}' is not + - * /")

# --- Parse the numbers safely ---
try:
    a = float(input("First number : "))
    b = float(input("Second number: "))
except ValueError:
    print("Those weren't both numbers. Bye!")
    raise SystemExit            # stop cleanly instead of crashing further

op = input("Operator (+ - * /): ").strip()

# --- Compute, catching each failure mode separately ---
try:
    result = calculate(a, b, op)
except ZeroDivisionError:
    print("Can't divide by zero!")
except UnknownOperatorError as e:
    print("Unknown operator:", e)
else:
    print(f"{a} {op} {b} = {result}")
finally:
    print("(thanks for using the safe calculator)")
