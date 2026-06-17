"""
Problem 01 - Seconds to H:M:S   (Day 1: numbers & operators)   [STUB]

Given a whole number of seconds, break it into hours, minutes and seconds.
Example: 3661 seconds  ->  (1, 1, 1)   i.e. 1 hour, 1 minute, 1 second.

Skills: integer division //, modulo %, returning a tuple.

Run:
    python q01_seconds_to_hms.py
"""

def to_hms(total_seconds):
    """Return (hours, minutes, seconds) for the given total_seconds."""
    # TODO: hours = how many whole 3600s fit in total_seconds  (use //)
    # TODO: take what's left over after the hours          (use %)
    # TODO: from the leftover, minutes = leftover // 60, seconds = leftover % 60
    # TODO: return (hours, minutes, seconds)
    pass


if __name__ == "__main__":
    print(to_hms(3661))    # expected: (1, 1, 1)
    print(to_hms(59))      # expected: (0, 0, 59)
