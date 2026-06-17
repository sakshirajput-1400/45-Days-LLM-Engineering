"""
Problem 11 - Temperature converter   (Day 5: functions & default args)   [STUB]

Write convert(temp, to="C") that converts a temperature.
  - to="F": Celsius -> Fahrenheit   (temp * 9/5 + 32)
  - to="C": Fahrenheit -> Celsius   ((temp - 32) * 5/9)
Round the result to 2 decimals. Default direction is "C".

Skills: def, parameters, a DEFAULT argument, if/elif/else, return.

Run:
    python q11_temperature_converter.py
"""

def convert(temp, to="C"):
    """Convert temp. to='F' means C->F; to='C' means F->C."""
    # TODO: if to == "F":  return round(temp * 9 / 5 + 32, 2)
    # TODO: elif to == "C": return round((temp - 32) * 5 / 9, 2)
    # TODO: else: return None  (unknown target)
    pass


if __name__ == "__main__":
    print(convert(100, to="F"))   # expected: 212.0
    print(convert(98.6))          # expected: 37.0  (default to="C")
