"""
Problem 12 - Number stats with *args   (Day 5: *args & return)   [STUB]

Write stats(*numbers) that accepts ANY number of arguments and returns a dict:
  {"min": ..., "max": ..., "avg": ...}
If no numbers are given, return None.
Example: stats(4, 8, 2, 6) -> {"min": 2, "max": 8, "avg": 5.0}

Skills: *args (collect args into a tuple), loop, min/max tracking, len(), return a dict.

Run:
    python q12_number_stats.py
"""

def stats(*numbers):
    """Return {'min','max','avg'} over the given numbers, or None if none."""
    # TODO: if there are no numbers, return None
    # TODO: track total, smallest, largest as you loop over `numbers`
    # TODO: avg = total / len(numbers)
    # TODO: return {"min": smallest, "max": largest, "avg": avg}
    pass


if __name__ == "__main__":
    print(stats(4, 8, 2, 6))   # expected: {'min': 2, 'max': 8, 'avg': 5.0}
    print(stats())             # expected: None
