# Hints — Expense Report

> **Rules:** 20 minutes of genuine attempt before Hint 1. Read **one** hint, then go back and try
> again. Scroll slowly — don't spoil the next hint.

<br><br><br><br><br>

---

## Hint 1 — restate the problem + choose your tools

Don't solve "the report." Solve **one line**. Write `parse_line(line)` that turns
`"2026-07-01,food,250"` into a record — a dict is a good shape:

```python
{"date": "2026-07-01", "category": "food", "amount": 250.0}
```

...and returns `None` for anything broken. Test it alone on a good line, a blank line, and
`"oops"` **before writing anything else**. Once one line works, the whole file is just a loop that
collects the non-`None` results.

<br><br><br><br><br>

---

## Hint 2 — the plan (function by function)

```
parse_line(line)   -> record or None
    strip the line; empty -> None
    split on ","; not exactly 3 parts -> None
    convert amount with float(); fails -> None      (try/except!)

load(text)         -> list of records
    for each line in text.splitlines(): parse it, keep the good ones

category_totals(records) -> dict
    the "counter with a dict" pattern: totals[cat] = totals.get(cat, 0) + amount

biggest(records)   -> the record with the max amount ("best so far" pattern)

report(records)    -> just prints: total = sum of amounts, average = total / count
```

Each function is 3–7 lines and testable on its own. That's the whole trick.

<br><br><br><br><br>

---

## Hint 3 — the trickiest lines only

Bad amounts must not crash — catch the failure and reject the line:

```python
try:
    amount = float(parts[2])
except ValueError:
    return None
```

The per-category accumulator without KeyErrors:

```python
totals[r["category"]] = totals.get(r["category"], 0) + r["amount"]
```

And guard the average: what should `report` do when there are **zero** records? (Remember the
divide-by-zero trap from the deck.) Now assemble the pieces.
