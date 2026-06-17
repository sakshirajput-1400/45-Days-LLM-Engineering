"""
Problem 11 - Temperature converter   (SOLUTION)

Run:
    python q11_temperature_converter_solution.py

Logic note:
  The `to="C"` default means callers can omit the direction for the common case.
  Passing it by name -- convert(100, to="F") -- reads clearly at the call site
  (keyword arguments, Day 5).
"""

def convert(temp, to="C"):
    """Convert temp. to='F' means C->F; to='C' means F->C."""
    if to == "F":
        return round(temp * 9 / 5 + 32, 2)
    elif to == "C":
        return round((temp - 32) * 5 / 9, 2)
    else:
        return None


if __name__ == "__main__":
    print("100 C -> F :", convert(100, to="F"))   # 212.0
    print("98.6 F -> C:", convert(98.6))          # 37.0 (uses default)
    print("0 C -> F   :", convert(0, to="F"))     # 32.0
    print("bad target :", convert(50, to="X"))    # None
