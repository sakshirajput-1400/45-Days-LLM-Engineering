"""Problem 1 stub - second largest distinct value, no sort().

Run:  python second_largest.py

RULE 1: fill in the # STEP comments in plain English BEFORE writing any code.
If you can't write the plan, that IS the gap - go re-read the problem, trace
an example by hand, and come back. Don't skip to typing.
"""


def second_largest(numbers):
    """Return the second largest DISTINCT value, or None if there isn't one."""
    # STEP 1 (Understand): input is ................. output is .................
    #                      "distinct" means [7, 7, 3] -> ........
    # STEP 2 (Example by hand): trace [72, 88, 65, 91, 88].
    #                      After each item, largest = ....  second = ....
    # STEP 3 (Plan): when a new number n arrives, the three cases are:
    #                      a) ...................................
    #                      b) ...................................
    #                      c) ...................................
    # STEP 4 (Code): translate your plan below, one comment line per plan step.

    pass  # TODO: your code here (delete this line)


# ---- STEP 5 (Test): run this file. All four lines should say OK. ----
if __name__ == "__main__":
    tests = [
        ([72, 88, 65, 91, 88], 88),
        ([7, 7, 3], 3),
        ([5], None),
        ([4, 4, 4], None),
    ]
    for numbers, expected in tests:
        got = second_largest(numbers)
        status = "OK " if got == expected else "FAIL"
        print(f"{status} second_largest({numbers}) -> {got} (expected {expected})")
