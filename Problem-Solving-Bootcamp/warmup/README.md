# Warm-up — Trace Before Write (15 minutes)

You cannot *generate* code you cannot *mentally execute*. This warm-up trains the simulation
muscle: for each snippet in [`warmup_trace.py`](warmup_trace.py), **predict the exact output on
paper first**, then run the file to check.

## How to do it

1. Open [`warmup_trace.py`](warmup_trace.py) in your editor. **Do not run it yet.**
2. For each of the 5 snippets, trace it line by line **on paper** — write down every variable's
   value as it changes, exactly like the computer would.
3. Write your predicted output for all 5 snippets.
4. Now run it and compare:

```bash
python warmup_trace.py
```

5. For every snippet you got wrong: don't shrug — **re-trace it** until you can explain *which
   line* your mental model got wrong.

## Why this matters

When you're stuck on a blank file, you're really doing two jobs at once: *inventing* steps and
*simulating* whether they'd work. If simulation is shaky, invention has nothing to check against.
Five minutes of prediction a day makes the simulator fast and trustworthy — and suddenly planning
gets much easier.

> Getting a prediction wrong here is the best outcome of the warm-up: you just found a precise gap
> in your mental model, for free, before it cost you an hour of debugging.

➡ Next: [`../problems/01-second-largest/`](../problems/01-second-largest/)
