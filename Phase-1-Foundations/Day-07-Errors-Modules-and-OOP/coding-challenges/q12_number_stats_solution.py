"""
Problem 12 - Number stats with *args   (SOLUTION)

Run:
    python q12_number_stats_solution.py

Logic note:
  *numbers packs every positional argument into a tuple, so the caller can pass
  as many as they like. Seed `smallest`/`largest` with the FIRST value (not 0),
  otherwise all-negative or all-large inputs would be wrong.
"""

def stats(*numbers):
    """Return {'min','max','avg'} over the given numbers, or None if none."""
    if not numbers:
        return None
    total = 0
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        total += n
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return {"min": smallest, "max": largest, "avg": total / len(numbers)}


if __name__ == "__main__":
    print(stats(4, 8, 2, 6))     # {'min': 2, 'max': 8, 'avg': 5.0}
    print(stats(-3, -1, -7))     # {'min': -7, 'max': -1, 'avg': ...}
    print(stats(42))             # {'min': 42, 'max': 42, 'avg': 42.0}
    print(stats())               # None
