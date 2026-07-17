# Hints — Run-Length Encoding

> **Rules:** 20 minutes of genuine attempt before Hint 1. Read **one** hint, then go back and try
> again. Scroll slowly — don't spoil the next hint.

<br><br><br><br><br>

---

## Hint 1 — restate the problem + choose your tools

While walking the string you must remember exactly two things:

- **which character** the current run is made of
- **how long** the run is so far

When the character you're looking at is *different* from the current run's character, a run just
**ended** — that's the moment you write `char + str(count)` onto your result (accumulator pattern),
then start a fresh run.

Trace `"aaabbc"` again with those two variables written on paper for every step.

<br><br><br><br><br>

---

## Hint 2 — the plan (pseudocode)

```
if text is empty: return ""
result = ""
run_char  = first character
run_count = 1
for each ch in the REST of the string:
    if ch is the same as run_char:
        run_count += 1
    else:
        append run_char and run_count to result   <- a run ended
        run_char, run_count = ch, 1               <- start the new run
append the LAST run to result                     <- don't forget this!
return result
```

Why the last line? Walk `"aaabbc"`: when the loop finishes, the `c1` run has *started* but nothing
ever told you it *ended*. Runs end when a different character arrives — and after the last
character, no one arrives.

<br><br><br><br><br>

---

## Hint 3 — the trickiest lines only

Slicing skips the first character so the loop starts from the second one:

```python
for ch in text[1:]:
```

Appending a finished run — note `str()`, because `count` is an `int`:

```python
result += run_char + str(run_count)
```

And the empty-string guard must come *before* you touch `text[0]`, or `""` crashes with an
`IndexError`. Now assemble it.
