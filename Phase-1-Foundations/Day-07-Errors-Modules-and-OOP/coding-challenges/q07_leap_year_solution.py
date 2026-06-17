"""
Problem 07 - Leap year check   (SOLUTION)

Run:
    python q07_leap_year_solution.py

Logic note:
  The whole rule is ONE boolean expression. The trap is the century years: 1900
  is divisible by 100 but not 400, so it is NOT a leap year; 2000 is divisible by
  400, so it IS. The parentheses keep the "and" group separate from the "or".
"""

def is_leap(year):
    """Return True if year is a leap year, else False."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


if __name__ == "__main__":
    for y in [2024, 1900, 2000, 2023, 1600, 2100]:
        print(f"{y} -> {is_leap(y)}")
