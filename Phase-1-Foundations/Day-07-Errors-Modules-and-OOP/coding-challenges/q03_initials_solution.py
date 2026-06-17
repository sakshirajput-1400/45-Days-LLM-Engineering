"""
Problem 03 - Initials from a name   (SOLUTION)

Run:
    python q03_initials_solution.py

Logic note:
  .split() with no argument breaks on any run of whitespace, so extra spaces
  are handled for free. word[0] is the first character; .upper() normalises it.
"""

def initials(full_name):
    """Return the dotted, upper-case initials of full_name."""
    result = ""
    for word in full_name.split():
        result += word[0].upper() + "."
    return result


if __name__ == "__main__":
    for name in ["asha ravi rao", "Sundar Pichai", "  ada   lovelace "]:
        print(f"{name!r:30} -> {initials(name)}")
