"""
Problem 14 - Compare two lists with sets   (SOLUTION)

Run:
    python q14_set_compare_solution.py

Logic note:
  Sets make "what's shared / unique / combined" a one-operator job: & (and),
  - (minus), | (or). Converting to a set also drops duplicates for free. We
  sorted() the results so the output is a predictable, readable list.
"""

def compare(list_a, list_b):
    """Return (common, only_a, combined) as sorted lists."""
    set_a = set(list_a)
    set_b = set(list_b)
    common = set_a & set_b
    only_a = set_a - set_b
    combined = set_a | set_b
    return (sorted(common), sorted(only_a), sorted(combined))


if __name__ == "__main__":
    a = [1, 2, 3, 4, 4]
    b = [3, 4, 5]
    common, only_a, combined = compare(a, b)
    print("common  :", common)
    print("only_a  :", only_a)
    print("combined:", combined)
