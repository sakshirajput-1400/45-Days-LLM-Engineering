"""
Problem 06 - Grade calculator   (SOLUTION)

Run:
    python q06_grade_calculator_solution.py

Logic note:
  Check the validity guard FIRST, then test bands from highest to lowest. Because
  elif stops at the first match, "marks >= 90" already implies "not < 75", so each
  band only needs its lower bound.
"""

def grade(marks):
    """Return the letter grade for marks, or 'Invalid' if out of range."""
    if marks < 0 or marks > 100:
        return "Invalid"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    for m in [100, 90, 89, 60, 40, 39, -5, 150]:
        print(f"{m:>4} -> {grade(m)}")
