# Hints — Caesar Cipher

> **Rules:** 20 minutes of genuine attempt before Hint 1. Read **one** hint, then go back and try
> again. Scroll slowly — don't spoil the next hint.

<br><br><br><br><br>

---

## Hint 1 — restate the problem + choose your tools

Work on **one character at a time** — write `shift_char(ch, shift)` first and test it alone.
The whole message is then just a loop that builds a new string (accumulator).

Tools you need:
- `ord("a")` → 97 turns a character into a number; `chr(97)` → `"a"` turns it back.
- `ch.islower()` / `ch.isupper()` tell you which alphabet you're in.
- The wrap-around: position 24 (`'y'`) + 3 = 27, and 27 needs to become 1. Which operator turns
  "too big" numbers back into the 0–25 range?

<br><br><br><br><br>

---

## Hint 2 — the plan (pseudocode)

```
shift_char(ch, shift):
    if ch is not a letter: return ch unchanged
    base = ord('a') if lowercase, ord('A') if uppercase
    position = ord(ch) - base          # now 0..25
    new_position = (position + shift) % 26     # shift WITH wrap-around
    return chr(base + new_position)

encrypt(text, shift):  join shift_char(ch, shift) for every ch
decrypt(text, shift):  encrypt with the OPPOSITE shift
```

Check the plan by hand before coding it: `'y'` → 24 → 27 → `27 % 26 = 1` → `'b'`. Works.
And why does `% 26` also make *negative* shifts work? (Python: `-2 % 26 == 24`.)

<br><br><br><br><br>

---

## Hint 3 — the trickiest lines only

```python
base = ord("a") if ch.islower() else ord("A")
return chr(base + (ord(ch) - base + shift) % 26)
```

And the decryption shortcut — shifting forward by 3 is undone by shifting forward by *minus* 3:

```python
def decrypt(text, shift):
    return encrypt(text, -shift)
```

Now write the "not a letter" guard and the loop in `encrypt`, and you're done.
