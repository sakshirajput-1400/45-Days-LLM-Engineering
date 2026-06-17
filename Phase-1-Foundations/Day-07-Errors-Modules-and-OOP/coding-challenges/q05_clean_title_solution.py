"""
Problem 05 - Clean & title-case a messy string   (SOLUTION)

Run:
    python q05_clean_title_solution.py

Logic note:
  .split() collapses ALL the extra whitespace in one step. .capitalize() makes
  the first letter upper and the REST lower (so "wORLD" -> "World"). Then join.
"""

def clean_title(messy):
    """Return messy with single spaces and each word capitalised."""
    words = messy.split()            # ["hELLo", "wORLD"]
    fixed = []
    for word in words:
        fixed.append(word.capitalize())
    return " ".join(fixed)


if __name__ == "__main__":
    samples = ["  hELLo    wORLD  ", "the  TODO   list", "PYTHON is FUN"]
    for s in samples:
        print(f"{s!r:24} -> {clean_title(s)!r}")
