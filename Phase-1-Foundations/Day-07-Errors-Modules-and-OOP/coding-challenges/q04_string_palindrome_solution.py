"""
Problem 04 - Palindrome check (strings)   (SOLUTION)

Run:
    python q04_string_palindrome_solution.py

Logic note:
  Normalise FIRST (lower-case + strip spaces) so "Race car" and "racecar" look
  the same. text[::-1] is the whole string with a step of -1 -> reversed.
"""

def is_palindrome(text):
    """Return True if text is a palindrome (ignoring case and spaces)."""
    cleaned = text.lower().replace(" ", "")   # method chaining (Day 2)
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    tests = ["Race car", "hello", "Nurses run", "Madam", "Python"]
    for t in tests:
        print(f"{t!r:14} -> {is_palindrome(t)}")
