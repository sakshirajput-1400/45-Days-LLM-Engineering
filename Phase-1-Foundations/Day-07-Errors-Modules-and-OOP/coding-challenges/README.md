# Day 07 — Coding Challenge Day (Days 1–6 recap) 🏋️

**15 problems** that exercise everything from the Python power-up week — **Days 1 to 6**. They're
**grouped by the day/topic** they test, so you can target a weak area or just work straight through.
Nothing here needs Day 7 material (no errors/OOP) — it's pure practice of the fundamentals.

## How to use this
1. **Read a problem**, then try it *before* peeking. Struggling first is how it sticks.
2. Stuck? Read the **Approach hint** under each problem — it nudges, it doesn't solve.
3. Write your answer in the **stub** (`qNN_*.py`, has `# TODO`s).
4. Check the worked **solution** (`qNN_*_solution.py`) — every one is runnable on its own and has a
   short *Logic note* explaining the key idea.

```bash
python q01_seconds_to_hms.py            # your attempt (stub)
python q01_seconds_to_hms_solution.py   # the worked answer
```

Every solution uses sample inputs in `if __name__ == "__main__":` — they run with **no typing required**.

## The map (15 problems, grouped by day)

| # | Problem | Day | Skills it drills |
|--:|---------|:---:|------------------|
| 01 | [Seconds to H:M:S](q01_seconds_to_hms.py) | 1 | `//`, `%`, tuples |
| 02 | [BMI calculator](q02_bmi_calculator.py) | 1 | `/`, `**`, `round()` |
| 03 | [Initials from a name](q03_initials.py) | 2 | `.split()`, indexing, `.upper()` |
| 04 | [Palindrome (string)](q04_string_palindrome.py) | 2 | `.lower()`, `.replace()`, `[::-1]` |
| 05 | [Clean & title-case](q05_clean_title.py) | 2 | `.split()`, `.capitalize()`, `.join()` |
| 06 | [Grade calculator](q06_grade_calculator.py) | 3 | comparisons, `if/elif/else` |
| 07 | [Leap year](q07_leap_year.py) | 3 | `and`/`or`/`not`, `%` |
| 08 | [Sum & count of digits](q08_digit_sum.py) | 4 | `while`, `//`, `%`, accumulator |
| 09 | [Star triangle](q09_pattern_triangle.py) | 4 | nested loops |
| 10 | [Fibonacci sequence](q10_fibonacci.py) | 4 | loop, list, simultaneous assignment |
| 11 | [Temperature converter](q11_temperature_converter.py) | 5 | functions, **default args** |
| 12 | [Number stats](q12_number_stats.py) | 5 | **`*args`**, return a dict |
| 13 | [Word frequency](q13_word_frequency.py) | 6 | **dict**, `.get()`, `.items()` |
| 14 | [Compare two lists](q14_set_compare.py) | 6 | **sets** `&` `-` `\|` |
| 15 | [Class gradebook](q15_gradebook.py) | 6+5 | dict-of-lists, stacking functions |

---

## Day 1 — Variables, numbers & operators

### Problem 01 — Seconds to H:M:S ⏱️
Break a count of seconds into `(hours, minutes, seconds)`. `3661 -> (1, 1, 1)`.
> **Approach hint:** Peel the biggest unit first. `hours = total // 3600`; keep the remainder with
> `% 3600`; then split that into minutes and seconds the same way.

### Problem 02 — BMI calculator ⚖️
`BMI = weight / height²`, rounded to 1 decimal. `72 kg, 1.75 m -> 23.5`.
> **Approach hint:** The `**` operator does powers, so `height_m ** 2` is height squared. Then divide
> and `round(value, 1)`.

---

## Day 2 — Strings, slicing & methods

### Problem 03 — Initials from a name 🔤
`"asha ravi rao" -> "A.R.R."`.
> **Approach hint:** `.split()` gives the words. For each word take `word[0]`, `.upper()` it, and tack
> on a `"."`. Build the result string as you go.

### Problem 04 — Palindrome (string) 🔁
Same forwards and backwards, ignoring case and spaces. `"Race car" -> True`.
> **Approach hint:** Normalise first — `.lower()` then `.replace(" ", "")` — so capitals and spaces
> don't fool you. Reverse with `cleaned[::-1]` and compare with `==`.

### Problem 05 — Clean & title-case 🧹
`"  hELLo    wORLD  " -> "Hello World"`.
> **Approach hint:** `.split()` with no argument collapses every run of spaces at once.
> `.capitalize()` fixes one word's casing; rejoin with `" ".join(...)`.

---

## Day 3 — Booleans & conditionals

### Problem 06 — Grade calculator 🎓
Marks → letter grade (A/B/C/D/F), `"Invalid"` if outside 0–100.
> **Approach hint:** Put the validity guard (`< 0 or > 100`) first, then test bands **highest-first**.
> Because `elif` stops at the first hit, each band only needs its lower bound.

### Problem 07 — Leap year 📅
Divisible by 4 and not 100, **or** divisible by 400. `1900 -> False`, `2000 -> True`.
> **Approach hint:** It's one boolean expression. Mind the century trap — keep the `and` group in its
> own parentheses, then `or (year % 400 == 0)`.

---

## Day 4 — Loops

### Problem 08 — Sum & count of digits 🔢
No strings: return `(sum_of_digits, digit_count)`. `4096 -> (19, 4)`.
> **Approach hint:** `n % 10` is the last digit; `n // 10` removes it. Loop `while n > 0`. Handle `0`
> specially — it never enters the loop but still has one digit.

### Problem 09 — Star triangle ⭐
Print a left-aligned triangle; row `r` has `r` stars.
> **Approach hint:** Two loops. The outer picks the row (`1..n`); the inner draws that many stars. The
> inner loop's length **depends on** the outer variable — that's the whole idea of nesting.

### Problem 10 — Fibonacci sequence 🌀
Return the first `count` Fibonacci numbers. `10 -> [0,1,1,2,3,5,8,13,21,34]`.
> **Approach hint:** Keep two variables and advance them together: `a, b = b, a + b`. Doing it on one
> line uses the *old* values on the right — splitting it into two lines would clobber `a` too early.

---

## Day 5 — Functions & scope

### Problem 11 — Temperature converter 🌡️
`convert(temp, to="C")` — C↔F, rounded to 2 decimals, default direction `"C"`.
> **Approach hint:** A **default argument** (`to="C"`) lets callers skip the common case. Branch on
> `to` with `if/elif/else`; return `None` for an unknown target.

### Problem 12 — Number stats 📈
`stats(*numbers)` → `{"min","max","avg"}`, or `None` if no args.
> **Approach hint:** `*numbers` collects all positional args into a tuple. Seed `smallest`/`largest`
> with the **first** value (not 0!), then loop. `avg = total / len(numbers)`.

---

## Day 6 — Data structures

### Problem 13 — Word frequency 🗣️
Count each word (case-insensitive); also find the most common. `"the cat the" -> {"the":2,"cat":1}`.
> **Approach hint:** `counts[word] = counts.get(word, 0) + 1` — `.get` returns 0 for an unseen word, so
> no `if` needed. For the top word, loop `.items()` with the "best so far" pattern.

### Problem 14 — Compare two lists 🔗
Return sorted `common`, `only_a`, `combined`. `[1,2,3,4] & [3,4,5]`.
> **Approach hint:** Turn both lists into `set(...)`, then it's one operator each: `&` (in both),
> `-` (only in A), `|` (everything). `sorted(...)` to get clean lists back.

### Problem 15 — Class gradebook 🏆 *(capstone — Days 5 + 6)*
`{name: [marks...]}` → per-student averages, and the topper.
> **Approach hint:** A dict whose values are lists. `sum(marks)/len(marks)` is one average. Have
> `topper()` **reuse** `averages()` instead of recomputing, then "best so far" for the max.

---

### Stretch goals (if you finish early)
- **H:M:S:** also print days for inputs over 24 hours.
- **Palindrome:** ignore punctuation too (`"A man, a plan, a canal: Panama"`).
- **Grade:** add `+`/`-` modifiers (e.g. 97+ → `A+`).
- **Digits:** return the digits as a list, and the product as well as the sum.
- **Fibonacci:** return only the *even* Fibonacci numbers below a limit.
- **Stats:** add `median` (sort the numbers, pick the middle).
- **Gradebook:** rank all students, and flag anyone below a pass mark.

➡ Back to the day: **[Day 07 README](../README.md)** · or revisit **[Day 05 logic-building](../../Day-05-Functions-and-Scope/logic-building/)** for the 5-step method.
