"""
Problem 14 - Compare two lists with sets   (Day 6: sets)   [STUB]

Given two lists, return three SORTED lists:
  - common:  items in BOTH       (set intersection &)
  - only_a:  items only in list_a (set difference -)
  - combined: every unique item   (set union |)
Example: [1,2,3,4] and [3,4,5] -> common [3,4], only_a [1,2], combined [1,2,3,4,5]

Skills: set(), & intersection, - difference, | union, sorted().

Run:
    python q14_set_compare.py
"""

def compare(list_a, list_b):
    """Return (common, only_a, combined) as sorted lists."""
    # TODO: turn both lists into sets
    # TODO: common = set_a & set_b ;  only_a = set_a - set_b ;  combined = set_a | set_b
    # TODO: return them as sorted() lists
    pass


if __name__ == "__main__":
    print(compare([1, 2, 3, 4], [3, 4, 5]))
    # expected: ([3, 4], [1, 2], [1, 2, 3, 4, 5])
