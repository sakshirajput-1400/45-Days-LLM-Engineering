# Problem-Solving Bootcamp — From "I understand it" to "I can write it"

> A standalone **3-hour practice session** about programming in general — not tied to any course day.
> Use it any time students say: *"When I see the solution I understand everything instantly...
> but I can't come up with it myself."*

That sentence describes the single most common wall in learning to program. It even has a nickname:
**tutorial hell**. This session explains *why* it happens and then makes you practice the way out.

> 🧠 **Start with the deck:** open [`presentation/index.html`](presentation/index.html) —
> *Why You Freeze at a Blank File*. It explains the core issue (reading code and writing code are
> two different muscles) and the 5 practice rules used below. **Watch it before touching the problems.**

---

## The core issue in one paragraph

Reading a solution is **recognition** — every line arrives with its context, and your brain only has
to say "yes, that step makes sense." Writing a solution is **generation** — you must *decompose* a
fuzzy problem into steps, *recall* the right construct for each step from a blank file, and
*sequence* them. Watching hundreds of solutions trains recognition and **zero** generation. That's
why the solution "makes sense in one go" (your recognition is fine!) while the blank file stays
blank (your generation never got any reps). The fix is not more explanations — it is **changing
what a practice rep is**: minutes spent stuck, planning and trying count; lines of solution read
do not.

## The 5 rules of this session (non-negotiable)

| # | Rule | Why |
|--:|------|-----|
| 1 | **Plan before code.** Write the steps in plain English as `# STEP` comments *before* any Python. | If you can't write the plan, you've found the real gap — and no syntax will fix it. |
| 2 | **20-minute struggle timer.** No hints, no solutions before 20 minutes of genuine attempt (plan on paper counts as attempting). | The stuck feeling *is* the exercise. Bailing out early skips the rep. |
| 3 | **Climb the hint ladder.** Each problem has a `HINTS.md` with 3 hints, weakest first. Read **one**, go back and try. | Hints unstick you without doing the decomposition for you. The solution is a last resort, not the next step. |
| 4 | **After reading a solution: close it and rewrite** the whole thing from a blank file, then do the **variant** in the problem README. | If the variant stumps you, you *recognized* the solution — you don't own it yet. |
| 5 | **Trace before write.** Do the warm-up first: predict output before running. | You can't generate code you can't mentally execute. |

## Session plan (3 hours)

| Time | Activity |
|------|----------|
| 0:00 – 0:30 | Deck: [`presentation/index.html`](presentation/index.html) — the why + the rules |
| 0:30 – 0:45 | [`warmup/`](warmup/) — 5 trace-before-write snippets (predict, then run) |
| 0:45 – 2:45 | [`problems/`](problems/) 1 → 5, rules in force. Trainers circulate; answer questions with *questions* ("what does step 2 of your plan say?"), not with code |
| 2:45 – 3:00 | Wrap-up: everyone picks one solved problem, closes the solution, rewrites it from blank (rule 4). Variants = homework |

## The problems (easiest → hardest)

Everything needs only core Python (variables, strings, loops, conditionals, functions, lists,
dicts). No libraries, no API keys, any language would work — Python is just what we use.

| # | Problem | The thinking skill it trains |
|--:|---------|------------------------------|
| 1 | [Second largest (no `sort()`)](problems/01-second-largest/) | Tracking *two* "best so far" values at once; duplicate edge cases |
| 2 | [Run-length encoding](problems/02-run-length-encoding/) | Spotting *group boundaries* while walking a string |
| 3 | [Balanced brackets](problems/03-balanced-brackets/) | Using a list as a *stack*; "most recent open must close first" |
| 4 | [Caesar cipher](problems/04-caesar-cipher/) | Characters as numbers; wrap-around with `%`; inverse operations |
| 5 | [Expense report](problems/05-expense-report/) | Real-world decomposition: parse → aggregate → report, one function per job |

Each problem folder contains:

```
problems/NN-name/
├── README.md        Problem statement, examples, a variant to do AFTER solving
├── HINTS.md         3 progressive hints — read ONE at a time
└── name.py          Stub with # STEP plan placeholders (rule 1 is built in)
```

> **Solutions are deliberately not in the repo.** The trainer shares them **after** the session —
> after the struggle timer, the hint ladder, and your own attempt (rules 2–4). That's not us being
> mean; the whole session is about what early solution-peeking does to your learning.

Run anything from inside its folder:

```bash
python second_largest.py
```

## For trainers

- The deck's speaker notes are in [`presentation/README.md`](presentation/README.md).
- The most important sentence to repeat all session: **"Stuck is not a signal that you're bad at
  this. Stuck is the rep."**
- When a student calls you over, ask to see their **plan** first. If there is no plan, that *is*
  the help they need — sit with them on steps, not on code.
- These rules transfer beyond this session: apply rules 1–4 to every `exercises/` folder in the
  course from now on.
