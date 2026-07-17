# Problem 3 — Balanced Brackets ⚖️

Given a string of brackets — `(` `)` `[` `]` `{` `}` — decide whether it is **balanced**: every
opener has a matching closer, in the right order. (This is literally what your editor and Python's
own parser do when they flag `SyntaxError: unexpected ')'`.)

```
"({[]})"  ->  True
"()[]{}"  ->  True
"(]"      ->  False   (wrong closer)
"(("      ->  False   (never closed)
")("      ->  False   (closer before opener)
""        ->  True    (nothing wrong with nothing)
```

**Thinking skill:** discovering that some problems need a **memory with an order** — the *most
recently opened* bracket must close *first*. A plain counter can't express that (trace `"(]"` with
a counter and watch it wrongly say True). The tool is a **stack**, and a Python list already is
one: `append()` to push, `pop()` to remove the most recent.

## Before you code (rule 1)

- **Understand:** what makes a string unbalanced? There are **three** distinct ways to fail — find
  all three in the examples above.
- **Example by hand:** trace `"({[]})"`. As you read each character, what does your brain keep
  track of? Write that "mental pile" down after every character.
- **Plan:** what happens when you see an opener? A closer? What must be true at the very end?

## Files

- Stub (start here): [`brackets.py`](brackets.py)
- Stuck after 20 minutes? [`HINTS.md`](HINTS.md) — one hint at a time
- Solution: shared by the trainer **after** the session (deliberately not in the repo)

## Variant — do this AFTER solving (rule 4)

Close your solution and, from a blank file, make it work on **real code lines**, ignoring
non-bracket characters: `is_balanced("print(nums[0])")` → `True`,
`is_balanced("f(x[1)]")` → `False`. One small change if you own the idea.

➡ Next: [`../04-caesar-cipher/`](../04-caesar-cipher/)
