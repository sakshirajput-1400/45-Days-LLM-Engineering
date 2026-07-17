# Problem 4 — Caesar Cipher 🔐

Encrypt text by shifting every letter forward in the alphabet by `shift` places, wrapping around
after `z`. Keep the letter's case; leave spaces, digits and punctuation untouched. (Julius Caesar
really used this — shift 3 — for military messages.)

```
encrypt("attack at dawn", 3)   ->  "dwwdfn dw gdzq"
encrypt("Hello, World!", 5)    ->  "Mjqqt, Btwqi!"
encrypt("xyz", 3)              ->  "abc"        (wrap-around!)
decrypt("dwwdfn dw gdzq", 3)   ->  "attack at dawn"
```

**Thinking skill:** treating characters as **numbers you can do maths on** (`ord`/`chr`), and using
`%` for **wrap-around** — the same trick behind clock arithmetic, circular buffers, and hashing.
Plus a beautiful shortcut: decryption is just... think about it.

## Before you code (rule 1)

- **Understand:** what exactly happens to `'y'` with shift 3? To `'Y'`? To `','`?
- **Example by hand:** number the alphabet a=0 … z=25. Shift `'y'` (24) by 3 → 27 → but there's no
  letter 27. What operation turns 27 into 1 (`'b'`)?
- **Plan:** for one character: how do you (1) detect it's a letter, (2) get its 0–25 position,
  (3) shift with wrap, (4) turn it back into a character *of the same case*?
- **Decompose:** if `shift_char(ch, shift)` handles one character, `encrypt` is just a loop —
  and `decrypt(text, 3)` is `encrypt(text, ?)`.

## Files

- Stub (start here): [`caesar.py`](caesar.py)
- Stuck after 20 minutes? [`HINTS.md`](HINTS.md) — one hint at a time
- Solution: shared by the trainer **after** the session (deliberately not in the repo)

## Variant — do this AFTER solving (rule 4)

Close your solution and write a **code breaker** from a blank file: given only
`"dwwdfn dw gdzq"` (shift unknown), print all 26 possible decryptions, one per line. A human can
spot the real message instantly — which teaches you *why* Caesar is a terrible cipher.

➡ Next: [`../05-expense-report/`](../05-expense-report/)
