"""
Problem 08 - Sum & count of digits   (SOLUTION)

Run:
    python q08_digit_sum_solution.py

Logic note:
  n % 10 is the LAST digit; n // 10 chops it off. Repeat until nothing is left.
  Edge case: 0 never enters a `while n > 0` loop, so handle it explicitly -- it
  still has one digit whose sum is 0.
"""

def digit_sum(n):
    """Return (sum_of_digits, digit_count) for a non-negative integer n."""
    if n == 0:
        return (0, 1)
    total = 0
    count = 0
    while n > 0:
        total += n % 10      # add the last digit
        n //= 10             # remove the last digit
        count += 1
    return (total, count)


if __name__ == "__main__":
    for value in [4096, 0, 7, 99999]:
        s, c = digit_sum(value)
        print(f"{value:>6} -> sum={s}, digits={c}")
