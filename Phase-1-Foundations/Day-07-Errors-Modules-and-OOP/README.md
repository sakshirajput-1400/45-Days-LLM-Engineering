# Day 07 — Errors, Modules & OOP

The final Python power-up day, and the bridge into real software. Three skills that separate "scripts
that work on my machine" from "code you'd ship":
- **Errors & exceptions** — programs *will* hit bad input, missing files, dead networks. Today you
  learn to catch failures and respond, instead of crashing. (Every LLM API call in Phase 1 is wrapped
  in `try/except`.)
- **Modules & pip** — stop reinventing the wheel. Import Python's batteries-included standard library,
  then install the world's open-source packages from PyPI (this is how you'll add `google-genai`,
  `requests`, `streamlit`).
- **OOP (classes)** — bundle related data *and* behaviour into your own types. Every library you'll
  touch (`ChatSession`, `Document`, `Agent`) is built from classes.

## Learning objectives
By the end of today you can:
- Name the **common exception types** and read a **traceback** to find what broke and where
- Handle failures with **`try` / `except` / `else` / `finally`** and catch *specific* exceptions
- **`raise`** your own exceptions (incl. a **custom exception class**) and choose **LBYL vs EAFP**
- **Import** from the standard library (`math`, `random`, `datetime`, `json`) with the main import styles
- Explain **pip / PyPI / `requirements.txt`** and import a third-party package **safely** (ImportError fallback)
- Define a **class** with `__init__`, instance **attributes** and **methods** (and `self`)
- Use **inheritance** and **`super()`** to extend a class without copy-pasting
- Write a **lambda** (one-line anonymous function) and pass it as `key=` to `sorted`/`max` and to `map`/`filter`

## Modules (work through them in order)

| # | Module | What it covers |
|--:|--------|----------------|
| 01 | [error-types](01-error-types/) | reading tracebacks; `NameError`/`TypeError`/`ValueError`/`IndexError`/`KeyError`/`ZeroDivisionError` |
| 02 | [try-except](02-try-except/) | `try`/`except`/`else`/`finally`, specific excepts, `raise`, custom exceptions, LBYL vs EAFP |
| 03 | [modules-and-imports](03-modules-and-imports/) | `import`, `from … import`, aliasing; `math`/`random`/`datetime`/`json` |
| 04 | [pip-and-third-party](04-pip-and-third-party/) | pip, PyPI, `requirements.txt`, venvs; safe third-party import |
| 05 | [classes-and-objects](05-classes-and-objects/) | `class`, `__init__`, attributes, creating instances, `self` |
| 06 | [instance-methods](06-instance-methods/) | methods, class vs instance attributes, `__str__` |
| 07 | [inheritance-and-super](07-inheritance-and-super/) | subclassing, overriding, `super()`, "is-a" |
| 08 | [lambda-functions](08-lambda-functions/) | one-line anonymous functions; `key=` with `sorted`/`max`; `map`/`filter` |

Then test yourself in **[exercises/](exercises/)**.

## The 5 things to really nail today
1. **Catch *specific* exceptions** (`except ValueError:`), not a bare `except:` that hides every bug.
2. **`finally` always runs** (cleanup); `else` runs only if no exception fired.
3. **`import` runs the module once** and gives you a namespace — `math.sqrt`, not `sqrt`.
4. **A class is a blueprint; an instance is one built object.** `__init__` sets up each instance;
   `self` is "this particular object."
5. **Inheritance = "is-a".** A `SavingsAccount` *is a* `BankAccount`; reuse with `super().__init__(...)`.

## How to run
From this folder, run any file directly:

```bash
python 01-error-types/error_types.py
```

The Safe Calculator exercise uses `input()`. Module 04 needs no internet — it *gracefully* handles a
missing package. For real installs, use the course CPython + pip (see the project README).

## Today's exercises
Three of them — see [`exercises/`](exercises/):
1. **Safe Calculator** — `try/except` + a custom exception around division and number parsing
2. **Bank Account** — a class with `__init__`, attributes, and `deposit`/`withdraw` methods
3. **Shapes & Inheritance** — a base `Shape` with `Rectangle`/`Circle` subclasses and `super()`

## 🏋️ Coding Challenge Day — recap Days 1–6
A bonus **[`coding-challenges/`](coding-challenges/)** set: **15 problems grouped by topic** (Days 1–6),
each with a stub + worked solution and an approach hint. Pure fundamentals practice — no Day-7 material
needed. Great for a dedicated practice session or homework.

➡ Next: **Phase 1 continues — Day 08: Python for AI** *(requests, dotenv, Pydantic, type hints)*
