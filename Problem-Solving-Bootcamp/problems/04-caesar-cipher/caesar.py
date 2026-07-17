"""Problem 4 stub - Caesar cipher.

Run:  python caesar.py

RULE 1: fill in the # STEP comments in plain English BEFORE writing any code.
"""


def shift_char(ch, shift):
    """Shift one character; non-letters pass through unchanged."""
    # STEP 1 (Understand): 'y' with shift 3 becomes .... , 'Y' becomes .... ,
    #                      ',' becomes ....
    # STEP 2 (Example by hand): a=0 ... z=25. 'y' is 24; 24+3=27; there is no
    #                      letter 27. Which operation fixes it, and to what?
    # STEP 3 (Plan): 1) detect a letter by ..............................
    #                2) get its 0-25 position by ........................
    #                3) shift with wrap by ..............................
    #                4) back to a character (same case) by ..............
    # STEP 4 (Code): translate your plan below.

    pass  # TODO: your code here (delete this line)


def encrypt(text, shift):
    """Shift every character of text."""
    # STEP 3 (Plan): with shift_char done, this is just the accumulator
    #                pattern over the string.

    pass  # TODO: your code here (delete this line)


def decrypt(text, shift):
    """Undo encrypt. HINT: it is a ONE-LINE call to encrypt. Think about it."""
    pass  # TODO: your code here (delete this line)


# ---- STEP 5 (Test): run this file. All four lines should say OK. ----
if __name__ == "__main__":
    tests = [
        (encrypt("attack at dawn", 3), "dwwdfn dw gdzq"),
        (encrypt("Hello, World!", 5), "Mjqqt, Btwqi!"),
        (encrypt("xyz", 3), "abc"),
        (decrypt("dwwdfn dw gdzq", 3), "attack at dawn"),
    ]
    for got, expected in tests:
        status = "OK " if got == expected else "FAIL"
        print(f'{status} got "{got}" (expected "{expected}")')
