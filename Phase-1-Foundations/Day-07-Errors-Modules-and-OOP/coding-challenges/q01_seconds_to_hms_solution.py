"""
Problem 01 - Seconds to H:M:S   (SOLUTION)

Run:
    python q01_seconds_to_hms_solution.py

Logic note:
  // gives the whole part of a division; % gives the remainder. Peel off the
  biggest unit first (hours), keep the remainder, then peel the next (minutes).
"""

def to_hms(total_seconds):
    """Return (hours, minutes, seconds) for the given total_seconds."""
    hours = total_seconds // 3600        # whole hours
    remaining = total_seconds % 3600     # seconds left after the hours
    minutes = remaining // 60            # whole minutes from the leftover
    seconds = remaining % 60             # final leftover seconds
    return (hours, minutes, seconds)


if __name__ == "__main__":
    for t in [3661, 86399, 59, 0]:
        h, m, s = to_hms(t)              # unpack the returned tuple
        print(f"{t:>6} sec = {h:02d}:{m:02d}:{s:02d}")
