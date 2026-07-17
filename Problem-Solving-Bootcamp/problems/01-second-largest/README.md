# Problem 1 — Second Largest (no `sort()`) 🥈

Given a list of exam scores, return the **second largest distinct value** — *without* using
`sort()`, `sorted()`, or `max()` twice on modified copies. One pass through the list.

```
[72, 88, 65, 91, 88]  ->  88
[7, 7, 3]             ->  3      (duplicates of the largest don't count)
[5]                   ->  None   (no second value exists)
[4, 4, 4]             ->  None   (only one distinct value)
```

**Thinking skill:** you already know "best so far" (one champion variable). This problem forces you
to run **two champions at once** — and to think carefully about *when* each one updates.

## Before you code (rule 1)

Answer these in the `# STEP` comments of the stub — in English, not Python:

- **Understand:** input = ? output = ? What exactly does "second largest **distinct**" mean when
  the list is `[7, 7, 3]`?
- **Example by hand:** walk `[72, 88, 65, 91, 88]` item by item. After each item, what are your
  "largest" and "second largest" on paper? *That table is your algorithm.*
- **Plan:** when a new number arrives, there are three interesting cases. What are they?

## Files

- Stub (start here): [`second_largest.py`](second_largest.py)
- Stuck after 20 minutes? [`HINTS.md`](HINTS.md) — one hint at a time
- Solution: shared by the trainer **after** the session (deliberately not in the repo)

## Variant — do this AFTER solving (rule 4)

Close your solution and, from a blank file, write **third largest** distinct value. Same idea,
three champions — if your understanding is real, this takes minutes. If it doesn't, you've learned
something important about the difference between recognizing and owning.

➡ Next: [`../02-run-length-encoding/`](../02-run-length-encoding/)
