"""Problem 2 stub - run-length encoding.

Run:  python rle.py

RULE 1: fill in the # STEP comments in plain English BEFORE writing any code.
"""


def encode(text):
    """Compress runs of repeated characters: "aaabbc" -> "a3b2c1"."""
    # STEP 1 (Understand): input is ............ output is ............
    #                      a run of length 1 becomes ........  "" becomes ........
    # STEP 2 (Example by hand): trace "aaabbc" char by char.
    #                      What two things must you remember during the walk?
    #                      When exactly does a run END?
    # STEP 3 (Plan): write the walk in plain English here:
    #                      ...................................
    #                      ...................................
    #                      (careful: how does the LAST run get written out?)
    # STEP 4 (Code): translate your plan below.

    pass  # TODO: your code here (delete this line)


# ---- STEP 5 (Test): run this file. All four lines should say OK. ----
if __name__ == "__main__":
    tests = [
        ("aaabbc", "a3b2c1"),
        ("aaaaaaaaaa", "a10"),
        ("abc", "a1b1c1"),
        ("", ""),
    ]
    for text, expected in tests:
        got = encode(text)
        status = "OK " if got == expected else "FAIL"
        print(f'{status} encode("{text}") -> "{got}" (expected "{expected}")')
