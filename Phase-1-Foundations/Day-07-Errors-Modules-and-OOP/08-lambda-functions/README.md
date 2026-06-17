# 08 — Lambda Functions

A **lambda** is a tiny, *anonymous* function written in a single line — no `def`, no name needed.
It's just a shorter way to write a small function. These two are exactly the same:

```python
def square(n):        # the familiar way
    return n * n

square = lambda n: n * n   # same function, as a one-line expression
```

The syntax is `lambda <args>: <expression>`. There's no `return` — whatever the expression evaluates
to *is* the result.

```python
add        = lambda a, b: a + b        # many args
full_name  = lambda first, last: first + " " + last
greet      = lambda: "Hello!"          # zero args
```

## Why bother? Functions that take other functions

Lambdas earn their keep when a function wants *another function* as an argument and writing a full
`def` would be overkill. The big four:

| Tool | What it does | Lambda example |
|------|--------------|----------------|
| `sorted(seq, key=…)` | sort by a custom measure | `sorted(students, key=lambda p: p[1])` — by marks |
| `max` / `min(seq, key=…)` | biggest/smallest *by what measure?* | `max(prices, key=lambda k: prices[k])` |
| `map(fn, seq)` | apply `fn` to every item | `map(lambda n: n*2, nums)` |
| `filter(fn, seq)` | keep items where `fn` is `True` | `filter(lambda n: n%2==0, nums)` |

```python
students = [("Asha", 88), ("Ravi", 72), ("Meena", 95)]
top = sorted(students, key=lambda pair: pair[1], reverse=True)   # by marks, high->low
```

Without the lambda you'd have to write a whole named helper function just to pull out `pair[1]` —
the lambda puts that logic right where it's used.

## Lambda vs `def` — when to use which

| Use a **lambda** when… | Use **`def`** when… |
|------------------------|---------------------|
| it's a *short, one-off* function | it has a name you'll reuse |
| it fits in a single expression | it needs multiple lines / statements |
| you're handing it to `sorted`/`map`/`filter`/`max` | it has real logic, loops, or `try/except` |

`map`/`filter` often read *better* as a **list comprehension** — know both:

```python
list(map(lambda n: n*2, nums))     # ==  [n*2 for n in nums]
list(filter(lambda n: n%2==0, nums))  # ==  [n for n in nums if n%2==0]
```

## 🎤 Talking points (what to say & focus on)
- **"A lambda is a function with the boring parts removed."** Same idea as `def`, no name and no
  `return` — just `lambda args: result`. Show the `square` pair side by side; that click is the lesson.
- **The payoff is `key=`.** Beginners ask "why not just use def?" — the honest answer is *you often
  should*. The one place lambdas truly shine is `sorted(..., key=...)` / `max(..., key=...)`. Lead with
  the "sort students by marks" demo; it's the most relatable.
- **`key=` answers "by what?"** Sort/max always need a measure. `key=lambda p: p[1]` literally reads
  "use the second item to compare." Tie it back to Day-6 lists/tuples.
- **`map`/`filter` vs comprehensions.** Show both producing the same list. Comprehensions usually win
  on readability in Python — but they'll *see* `map`/`filter` in others' code, so demystify them.
- **AI tie-in:** you'll pass small lambdas as `key=` to rank search results by score in Phase 2 (RAG),
  and frameworks take callbacks you can supply as lambdas. It's a small tool you'll reach for often.

## ⚠️ Common mistakes to call out
- **Naming a lambda** (`f = lambda x: ...`) when you could just write `def f(x):` — if it needs a name,
  use `def`. (Style checkers flag exactly this.)
- Trying to put a **statement** inside a lambda (`lambda x: print(x); return x`) — lambdas hold *one
  expression*, nothing more. Reach for `def`.
- **Forgetting `list(...)`** around `map`/`filter` — they return lazy iterators, so `print(map(...))`
  shows `<map object>` not the values.
- Cramming **too much logic** into a lambda until it's unreadable — past one expression, switch to `def`.

Run the examples:

```bash
python lambda_functions.py
```

➡ Next: **[exercises/](../exercises/)** — Safe Calculator, Bank Account & Shapes (inheritance)
