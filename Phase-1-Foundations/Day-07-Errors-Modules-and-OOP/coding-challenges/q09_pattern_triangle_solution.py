"""
Problem 09 - Star triangle pattern   (SOLUTION)

Run:
    python q09_pattern_triangle_solution.py

Logic note:
  Two loops: the OUTER one picks the row, the INNER one draws that row. The link
  between them is that row r needs r stars -- the inner loop's length depends on
  the outer loop's variable. That dependency is the heart of nested loops.
"""

def triangle(n):
    """Print a star triangle with n rows."""
    for r in range(1, n + 1):        # outer loop: one pass per row
        line = ""
        for _ in range(r):           # inner loop: r stars on this row
            line += "* "
        print(line.rstrip())         # rstrip drops the trailing space


if __name__ == "__main__":
    print("--- n = 4 ---")
    triangle(4)
    print("--- n = 6 ---")
    triangle(6)
