"""
Problem 04 - Palindrome check (strings)   (Day 2: slicing & methods)   [STUB]

A palindrome reads the same forwards and backwards, ignoring case and spaces.
Examples: "Race car" -> True,  "hello" -> False,  "Nurses run" -> True.

Skills: .lower(), .replace(), reverse slicing [::-1], == comparison.

Run:
    python q04_string_palindrome.py
"""

def is_palindrome(text):
    """Return True if text is a palindrome (ignoring case and spaces)."""
    # TODO: make a cleaned version: lower-case it, then remove spaces (.replace(" ", ""))
    # TODO: reverse it with slicing  cleaned[::-1]
    # TODO: return whether cleaned == its reverse
    pass


if __name__ == "__main__":
    print(is_palindrome("Race car"))    # expected: True
    print(is_palindrome("hello"))       # expected: False
