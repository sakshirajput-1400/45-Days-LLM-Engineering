# Hints — Balanced Brackets

> **Rules:** 20 minutes of genuine attempt before Hint 1. Read **one** hint, then go back and try
> again. Scroll slowly — don't spoil the next hint.

<br><br><br><br><br>

---

## Hint 1 — restate the problem + choose your tools

The key rule: **the most recently opened bracket must be the first one to close.**

So you need to remember all the currently-open brackets *in order*, and always look at the newest
one. A Python list does exactly this: `pile.append(x)` puts on top, `pile.pop()` takes off the top.
(This shape is called a *stack*.)

Trace `"({[]})"` keeping such a pile on paper: what goes on when you see `(`? What comes off (and
what must it match) when you see `]`?

<br><br><br><br><br>

---

## Hint 2 — the plan (pseudocode)

```
pile = empty list
for each ch in the string:
    if ch is an opener:
        push it on the pile
    if ch is a closer:
        if the pile is empty        -> False   (closer with nothing open)
        pop the top of the pile
        if it isn't the matching opener -> False   (wrong closer)
balanced only if the pile is EMPTY at the end     (nothing left open)
```

Note there are **three** ways to return False — match them to `")("`, `"(]"`, and `"(("`.
A dict makes "the matching opener" easy: `pairs = {")": "(", "]": "[", "}": "{"}`.

<br><br><br><br><br>

---

## Hint 3 — the trickiest lines only

```python
pairs = {")": "(", "]": "[", "}": "{"}

if ch in pairs:                    # ch is a closer
    if not pile:                   # nothing open -> fail
        return False
    if pile.pop() != pairs[ch]:    # top of pile must be its opener
        return False
```

And the last line of the function is just `return not pile` — True only when nothing is left open.
Now write the opener case and assemble it.
