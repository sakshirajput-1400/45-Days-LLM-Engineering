# 02 — `try` / `except` (Handling & Raising Errors)

Catching exceptions lets your program **recover** instead of crashing. This is the difference between
an app that dies on one bad input and one that says "please enter a number" and carries on.

```python
try:
    age = int(input("Age: "))      # might raise ValueError
except ValueError:
    print("That wasn't a number.") # runs only if a ValueError fired
```

## The full shape: `try` / `except` / `else` / `finally`
```python
try:
    data = risky()                 # the code that might fail
except FileNotFoundError:
    print("file missing")          # handle a SPECIFIC error
except (TypeError, ValueError) as e:
    print("bad data:", e)          # handle several; `as e` grabs the object
else:
    print("worked:", data)         # runs ONLY if no exception was raised
finally:
    print("always runs")           # cleanup — runs no matter what
```

| Block | Runs when |
|-------|-----------|
| `try` | always (the protected code) |
| `except` | an exception of that type was raised |
| `else` | the `try` finished with **no** exception |
| `finally` | **always**, exception or not (close files, release locks) |

## Catch *specific* exceptions
```python
except:            # ❌ bare — hides typos, KeyboardInterrupt, everything
except Exception:  # broad, but at least named
except ValueError: # ✅ catch exactly what you expect to handle
```
A bare `except:` swallows bugs and makes debugging miserable. Catch what you can actually handle.

## Raise your own — and make a custom exception
```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")    # signal a problem
    return balance - amount

class InsufficientFundsError(Exception):           # your own error type
    """Raised when a withdrawal exceeds the balance."""
```
A custom exception class (just inherit from `Exception`) lets callers catch *your* specific error.

## LBYL vs EAFP (two valid styles)
- **LBYL** — *Look Before You Leap*: check first. `if key in d: ...`
- **EAFP** — *Easier to Ask Forgiveness than Permission*: just try it, handle the failure.
  `try: d[key] except KeyError: ...`

Python leans **EAFP** — it's often cleaner and avoids race conditions (the thing can change between
the check and the use). Use LBYL for cheap, simple guards.

## 🎤 Talking points (what to say & focus on)
- **"try = attempt, except = plan B."** The `int(input())` recovery demo is the hook — turn a crash
  into a polite re-prompt. Instantly relatable.
- **Specific excepts, always.** Show a bare `except:` hiding a typo'd variable name (the program
  "works" but silently does nothing). Then narrow it to `except ValueError`. The bug reappears —
  which is *good*. This is the most important habit of the module.
- **`finally` always runs** — even after a `return` or an uncaught error. Frame it as "cleanup that
  must happen" (close the file, release the connection). Demo it firing on both paths.
- **`raise` is you being the messenger.** Validate inputs and `raise ValueError(...)` early (ties to
  Day-5 guard clauses). Then a custom `class FooError(Exception)` so callers catch *your* error.
- **EAFP is the Pythonic default**, and it's exactly how you'll wrap LLM/API calls in Phase 1:
  `try: call_api() except RateLimitError: backoff()`. Make that connection explicit.

## ⚠️ Common mistakes to call out
- Bare `except:` (or `except Exception:` everywhere) → hides real bugs.
- Putting too much inside one `try` so you can't tell which line failed.
- Catching an exception and doing nothing (`except: pass`) — silent failure.
- Using `except` for normal control flow that a simple `if` would handle better.

Run the examples:

```bash
python try_except.py
```

➡ Next: **[03-modules-and-imports](../03-modules-and-imports/)**
