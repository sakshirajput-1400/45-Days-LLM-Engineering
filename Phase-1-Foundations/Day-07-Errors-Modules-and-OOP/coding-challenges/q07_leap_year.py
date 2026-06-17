"""
Problem 07 - Leap year check   (Day 3: logical operators)   [STUB]

A year is a leap year if:
  - it is divisible by 4 AND not divisible by 100, OR
  - it is divisible by 400.
Examples: 2024 -> True, 1900 -> False, 2000 -> True, 2023 -> False.

Skills: modulo %, and / or / not, returning a boolean.

Run:
    python q07_leap_year.py
"""

def is_leap(year):
    """Return True if year is a leap year, else False."""
    # TODO: divisible by 4 and not by 100  ->  (year % 4 == 0 and year % 100 != 0)
    # TODO: OR divisible by 400            ->  or (year % 400 == 0)
    # TODO: return that single boolean expression
    pass


if __name__ == "__main__":
    print(is_leap(2024))   # True
    print(is_leap(1900))   # False
    print(is_leap(2000))   # True
