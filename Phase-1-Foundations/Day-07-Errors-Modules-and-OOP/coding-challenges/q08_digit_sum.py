"""
Problem 08 - Sum & count of digits   (Day 4: while loop)   [STUB]

Without converting to a string, return (sum_of_digits, number_of_digits).
Example: 4096  ->  (19, 4)   because 4+0+9+6 = 19 and it has 4 digits.

Skills: while loop, last digit n % 10, drop last digit n // 10, accumulator + counter.

Run:
    python q08_digit_sum.py
"""

def digit_sum(n):
    """Return (sum_of_digits, digit_count) for a non-negative integer n."""
    # TODO: special-case n == 0 -> (0, 1)
    # TODO: start total = 0 and count = 0
    # TODO: while n > 0:  add n % 10 to total, do n = n // 10, count += 1
    # TODO: return (total, count)
    pass


if __name__ == "__main__":
    print(digit_sum(4096))   # expected: (19, 4)
    print(digit_sum(0))      # expected: (0, 1)
