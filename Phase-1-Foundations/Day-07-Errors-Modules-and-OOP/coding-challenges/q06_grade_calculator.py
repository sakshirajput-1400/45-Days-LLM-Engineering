"""
Problem 06 - Grade calculator   (Day 3: conditionals)   [STUB]

Turn a marks value (0-100) into a letter grade:
  90+ -> A,  75-89 -> B,  60-74 -> C,  40-59 -> D,  below 40 -> F
Anything outside 0-100 -> "Invalid".

Skills: comparison operators, if/elif/else, boundary thinking.

Run:
    python q06_grade_calculator.py
"""

def grade(marks):
    """Return the letter grade for marks, or 'Invalid' if out of range."""
    # TODO: first reject out-of-range marks (< 0 or > 100) -> "Invalid"
    # TODO: then check the HIGHEST band first (>= 90 -> "A")
    # TODO: work downwards with elif: 75, 60, 40
    # TODO: else -> "F"
    pass


if __name__ == "__main__":
    print(grade(95))    # A
    print(grade(72))    # C
    print(grade(150))   # Invalid
