"""
Common error (exception) types — triggered on purpose, caught, and explained.

We catch each one so the file runs top-to-bottom and you SEE every message,
instead of stopping at the first crash.

Run:
    python error_types.py
"""

# A tiny helper so each demo prints the error TYPE and MESSAGE cleanly.
def show(label, func):
    try:
        func()
    except Exception as e:                      # catch any error just for the demo
        print(f"{label:<20} -> {type(e).__name__}: {e}")

# =====================================================================
# Runtime errors — they fire WHILE the program runs
# =====================================================================
show("NameError",         lambda: print(undefined_variable))       # never defined
show("TypeError",         lambda: "3" + 5)                          # str + int
show("ValueError",        lambda: int("abc"))                       # right type, bad value
show("IndexError",        lambda: [1, 2, 3][10])                    # out of range
show("KeyError",          lambda: {"a": 1}["b"])                    # missing dict key
show("ZeroDivisionError", lambda: 1 / 0)                            # divide by zero
show("AttributeError",    lambda: "hello".push("!"))                # strings have no push()
show("FileNotFoundError", lambda: open("does_not_exist_12345.txt")) # missing file

print()

# =====================================================================
# ValueError vs TypeError — the subtle pair worth understanding
# =====================================================================
# TypeError  = wrong TYPE for the operation
# ValueError = right type, but the VALUE doesn't make sense
show("int('abc')",  lambda: int("abc"))      # ValueError: can't parse those chars
show("len(5)",      lambda: len(5))          # TypeError: an int has no length
print()

# =====================================================================
# What an UNCAUGHT error looks like (commented so the file keeps running)
# =====================================================================
# Uncomment the next line to see a real traceback printed by Python:
#   result = 10 / 0
# It would print:
#   Traceback (most recent call last):
#     File "error_types.py", line N, in <module>
#       result = 10 / 0
#   ZeroDivisionError: division by zero
# Read it BOTTOM-UP: last line = what broke; line above = where.
print("Tip: read tracebacks bottom-up - the last line is the headline.")
print("Module 02 shows how to CATCH these so your program recovers.")
