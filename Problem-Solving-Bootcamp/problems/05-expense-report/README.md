# Problem 5 — Expense Report 🧾

The final boss — not because any single step is hard, but because **nobody tells you the steps**.
This is what real programming tasks look like: a messy blob of data and a vague request.

You get a month of UPI-style expenses as raw text, one per line, in the format
`date,category,amount`. Blank lines and malformed lines (missing fields, non-numeric amount) must
be **skipped**, not crash the program.

```
2026-07-01,food,250
2026-07-02,travel,120

2026-07-03,food,90
oops this line is broken
2026-07-04,rent,8000
2026-07-05,food,310.50
2026-07-06,travel,4x0        <- bad amount: skip it
```

Produce a report with:

1. the **total** spent
2. spending **per category** (a dict)
3. the **single biggest** expense (its date, category and amount)
4. the **average** transaction amount

**Thinking skill:** *decomposition itself*. A blob-task becomes easy the moment you split it into
one-job functions: `parse_line` → `load` → `category_totals` / `biggest` / stats. Solve and test
each alone — exactly how the course's Day 20 `docchat/` package is built, and how you should
approach every project from now on.

## Before you code (rule 1)

- **Understand:** what is a *record*? Pick a shape for one parsed line (tuple? dict?) and write it
  down. What exactly makes a line "bad"?
- **Example by hand:** parse the sample above on paper. How many good records? Total? Which line
  is the biggest?
- **Plan:** name your functions *before writing any of them*. One job each. Which one do you
  build and test first?

## Files

- Stub (start here): [`expense_report.py`](expense_report.py)
- Stuck after 20 minutes? [`HINTS.md`](HINTS.md) — one hint at a time
- Solution: shared by the trainer **after** the session (deliberately not in the repo)

## Variant — do this AFTER solving (rule 4)

Close your solution and add, from memory: **spending for one given month** — a function
`month_total(records, "2026-07")` that sums only matching dates. Then print the category the user
spends the most on. If your functions were truly one-job, this slots in without touching them.
