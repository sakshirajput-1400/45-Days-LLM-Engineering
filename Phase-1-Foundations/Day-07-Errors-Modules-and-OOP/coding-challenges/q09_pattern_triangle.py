"""
Problem 09 - Star triangle pattern   (Day 4: nested loops)   [STUB]

Print a left-aligned triangle of stars with n rows. For n = 4:
    *
    * *
    * * *
    * * * *
Row r has exactly r stars.

Skills: nested loops (outer = rows, inner = stars), building a line string.

Run:
    python q09_pattern_triangle.py
"""

def triangle(n):
    """Print a star triangle with n rows."""
    # TODO: outer loop r from 1 to n         -> for r in range(1, n + 1):
    # TODO:   build a line: inner loop adds "* " r times
    # TODO:   print the line (use .rstrip() to drop the trailing space)
    pass


if __name__ == "__main__":
    triangle(4)
