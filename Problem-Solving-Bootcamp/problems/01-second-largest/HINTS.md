# Hints — Second Largest

> **Rules:** 20 minutes of genuine attempt before Hint 1. Read **one** hint, then go back and try
> again. Scroll slowly — don't spoil the next hint.

<br><br><br><br><br>

---

## Hint 1 — restate the problem + choose your tools

You are looking for the champion **and** the runner-up in a single walk through the list.
So you need **two** variables: `largest` and `second`. Start both as `None` ("nothing seen yet").

The heart of the problem: when a new number `n` arrives, what should happen to those two variables?
Go trace `[72, 88, 65, 91, 88]` by hand and watch what *your brain* does with the two values.

<br><br><br><br><br>

---

## Hint 2 — the plan (pseudocode)

For each number `n` in the list, there are exactly three cases:

```
if n is bigger than largest:
    the old largest becomes the new second
    n becomes the new largest
otherwise, if n is smaller than largest but bigger than second:
    n becomes the new second
otherwise:
    do nothing
```

Careful with the middle case: why must it be **strictly smaller** than `largest`?
(Trace `[7, 7, 3]` to see — this is where duplicates get handled.)

<br><br><br><br><br>

---

## Hint 3 — the trickiest lines only

Comparing numbers against `None` crashes, so each comparison needs an "or nothing yet" escape:

```python
if largest is None or n > largest:
    second = largest
    largest = n
elif n != largest and (second is None or n > second):
    second = n
```

The `n != largest` is the whole duplicates fix. Now finish the function yourself: what do you
return, and what does `[5]` return automatically?
