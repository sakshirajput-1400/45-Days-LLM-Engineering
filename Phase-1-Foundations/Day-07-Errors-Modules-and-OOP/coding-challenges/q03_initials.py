"""
Problem 03 - Initials from a name   (Day 2: strings)   [STUB]

Turn a full name into upper-case dotted initials.
Example: "asha ravi rao"  ->  "A.R.R."

Skills: .split(), indexing word[0], .upper(), building a string.

Run:
    python q03_initials.py
"""

def initials(full_name):
    """Return the dotted, upper-case initials of full_name."""
    # TODO: split the name into words with .split()
    # TODO: start with an empty result string
    # TODO: for each word, add its FIRST letter (upper-cased) + "."
    # TODO: return the result
    pass


if __name__ == "__main__":
    print(initials("asha ravi rao"))   # expected: A.R.R.
    print(initials("Sundar Pichai"))   # expected: S.P.
