# Problem 2 — Run-Length Encoding 📦

Compress a string by replacing each **run** of repeated characters with the character followed by
its count. (This is a real compression idea — old fax machines and image formats used it.)

```
"aaabbc"      ->  "a3b2c1"
"aaaaaaaaaa"  ->  "a10"
"abc"         ->  "a1b1c1"
""            ->  ""
```

**Thinking skill:** walking a sequence while noticing **group boundaries** — "this character is
different from the previous one, so a run just ended." A huge number of real problems (log
grouping, streak counting, data cleaning) are this exact shape.

## Before you code (rule 1)

- **Understand:** input = ? output = ? What should a run of length 1 become? The empty string?
- **Example by hand:** trace `"aaabbc"` character by character on paper. At each character write:
  *what run am I in, how long is it so far, did a run just end?* Notice the awkward moment: how do
  you know the **last** run ended?
- **Plan:** what two things must you remember while walking the string?

## Files

- Stub (start here): [`rle.py`](rle.py)
- Stuck after 20 minutes? [`HINTS.md`](HINTS.md) — one hint at a time
- Solution: shared by the trainer **after** the session (deliberately not in the repo)

## Variant — do this AFTER solving (rule 4)

Close your solution and write the **decoder** from a blank file: `"a3b2c1"` → `"aaabbc"`.
It's a different walk (read a letter, then read its digits — careful, counts can be `10+`), and it
proves you understood the format, not just the loop.

➡ Next: [`../03-balanced-brackets/`](../03-balanced-brackets/)
