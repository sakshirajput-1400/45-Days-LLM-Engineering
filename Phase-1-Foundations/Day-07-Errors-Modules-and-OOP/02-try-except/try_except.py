"""
try / except / else / finally, catching specific errors, raising your own.

Run:
    python try_except.py
"""

# =====================================================================
# 1) The basic recovery: turn a crash into a graceful message
# =====================================================================
def to_int(text):
    try:
        return int(text)                 # might raise ValueError
    except ValueError:
        return None                      # plan B: signal "couldn't parse"

print("to_int('42') :", to_int("42"))
print("to_int('abc'):", to_int("abc"))   # no crash — we handled it
print()

# =====================================================================
# 2) The full shape: try / except / else / finally
# =====================================================================
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"  {a}/{b}: cannot divide by zero")
    else:
        print(f"  {a}/{b} = {result}")   # runs ONLY if no exception
    finally:
        print("  (finally: this always runs)")   # cleanup, always

safe_divide(10, 2)
safe_divide(10, 0)
print()

# =====================================================================
# 3) Catch SPECIFIC exceptions (not a bare except that hides bugs)
# =====================================================================
def parse_record(text):
    try:
        name, age = text.split(",")      # could raise ValueError (wrong shape)
        return name.strip(), int(age)    # int() could also raise ValueError
    except ValueError as e:
        return None, f"bad record ({e})"

print("parse 'Asha, 21'  :", parse_record("Asha, 21"))
print("parse 'broken'    :", parse_record("broken"))
print()

# =====================================================================
# 4) RAISE your own errors — validate inputs early (Day-5 guard clause)
# =====================================================================
class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the available balance."""

def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(f"need {amount}, have {balance}")
    return balance - amount

# A caller can now catch OUR specific exception:
for attempt in (300, 5000, -10):
    try:
        new_balance = withdraw(1000, attempt)
        print(f"withdrew {attempt} -> balance {new_balance}")
    except InsufficientFundsError as e:
        print(f"withdrew {attempt} -> declined: {e}")
    except ValueError as e:
        print(f"withdrew {attempt} -> invalid: {e}")
print()

# =====================================================================
# 5) LBYL vs EAFP — two valid styles for the same goal
# =====================================================================
stock = {"apple": 5, "banana": 0}

# LBYL — "Look Before You Leap": check first
item = "cherry"
if item in stock:
    print("LBYL:", stock[item])
else:
    print("LBYL: not stocked")

# EAFP — "Easier to Ask Forgiveness": just try, handle the failure (Pythonic)
try:
    print("EAFP:", stock[item])
except KeyError:
    print("EAFP: not stocked")
# In Phase 1 you'll wrap API calls EAFP-style:
#   try: response = call_llm(prompt)
#   except RateLimitError: time.sleep(backoff); retry...
