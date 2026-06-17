# 01 — Error Types & Reading Tracebacks

When Python hits something it can't do, it **raises an exception** and (if nobody catches it) prints a
**traceback** and stops. Errors aren't failure — they're Python *telling you exactly what's wrong*.
Step one is learning to read that message.

## Read a traceback bottom-up
```
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    total = price / count
            ~~~~~~^~~~~~~
ZeroDivisionError: division by zero
```
- **Last line** = the *type* and *message* (the what). Read this first.
- **Above it** = the *file and line* (the where).
- Multiple frames = the call chain (read bottom = where it blew up).

## The common exceptions you'll actually meet
| Exception | Means | Classic cause |
|-----------|-------|---------------|
| `SyntaxError` | code is malformed | missing `:` or `)` — caught *before* running |
| `NameError` | name not defined | typo, or used before assignment |
| `TypeError` | wrong type for the operation | `"3" + 5`, calling a non-function |
| `ValueError` | right type, bad value | `int("abc")` |
| `IndexError` | list index out of range | `items[10]` on a 3-item list |
| `KeyError` | dict key missing | `d["nope"]` |
| `ZeroDivisionError` | divide by zero | `x / 0` |
| `FileNotFoundError` | file isn't there | opening a missing path |
| `AttributeError` | no such attribute/method | `"hi".push()` |

**`SyntaxError` is different** — it's raised while Python is *parsing* the file, before any line runs.
The rest are **runtime** errors (they fire while the program executes).

## 🎤 Talking points (what to say & focus on)
- **"An exception is Python telling you what's wrong — for free."** Reframe errors from scary to
  helpful. The traceback is a map, not a punishment.
- **Read bottom-up, every time.** The last line (type + message) is the headline; the line above is
  the address. Drill this — beginners freeze at the wall of text instead of reading the bottom line.
- **Match the message to the cause.** Run each error live (the demo file does), read its name, and
  ask "what would cause this?" Building the type→cause reflex saves them hours of debugging.
- **SyntaxError vs the rest.** Syntax errors stop the file from *starting*; runtime errors happen
  *during* a run (so earlier prints still appear). That distinction explains a lot of confusion.
- **`ValueError` vs `TypeError`** is the subtle one: wrong *value* of the right type vs wrong *type*
  entirely. `int("abc")` is ValueError; `"a" + 1` is TypeError. Worth one clear example.

## ⚠️ Common mistakes to call out
- Panicking at the traceback instead of reading the last line.
- Confusing `ValueError` (bad value) with `TypeError` (wrong type).
- Editing the wrong file/line because they didn't read the "File … line …" part.
- Assuming a `SyntaxError` is a logic bug — it's a typo Python caught before running.

Run the examples (this file deliberately triggers and catches errors to show their messages):

```bash
python error_types.py
```

➡ Next: **[02-try-except](../02-try-except/)**
