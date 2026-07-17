"""Problem 3 stub - balanced brackets.

Run:  python brackets.py

RULE 1: fill in the # STEP comments in plain English BEFORE writing any code.
"""


def is_balanced(text):
    """Return True if every bracket opens and closes correctly, in order."""
    # STEP 1 (Understand): the THREE different ways a string can fail are:
    #                      a) ............ (example: ........)
    #                      b) ............ (example: ........)
    #                      c) ............ (example: ........)
    # STEP 2 (Example by hand): trace "({[]})". What does your brain keep
    #                      track of after each character? Write the pile down.
    # STEP 3 (Plan): on an opener I will ..............................
    #                on a closer I will ...............................
    #                at the very end, balanced means ..................
    # STEP 4 (Code): translate your plan below.

    pass  # TODO: your code here (delete this line)


# ---- STEP 5 (Test): run this file. All six lines should say OK. ----
if __name__ == "__main__":
    tests = [
        ("({[]})", True),
        ("()[]{}", True),
        ("(]", False),
        ("((", False),
        (")(", False),
        ("", True),
    ]
    for text, expected in tests:
        got = is_balanced(text)
        status = "OK " if got == expected else "FAIL"
        print(f'{status} is_balanced("{text}") -> {got} (expected {expected})')
