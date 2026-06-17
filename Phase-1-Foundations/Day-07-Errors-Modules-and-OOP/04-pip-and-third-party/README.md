# 04 — pip & Third-Party Packages

The standard library is huge, but the *real* superpower is **PyPI** (the Python Package Index) — 500k+
open-source packages you install with **pip**. This is how you'll add `google-genai`, `requests`,
`streamlit`, `chromadb` in the AI track. Almost every line of this course's Phase 1+ depends on it.

## The workflow
```bash
pip install requests              # download & install from PyPI
pip install requests==2.31.0      # a specific version (reproducible)
pip list                          # what's installed
pip freeze > requirements.txt     # snapshot exact versions
pip install -r requirements.txt   # recreate the same environment elsewhere
```
> On this course's Windows setup, use the real CPython's pip:
> `C:\Users\PC\AppData\Local\Programs\Python\Python312\python.exe -m pip install <pkg>`
> (`python -m pip` is the safest form — it installs into *that* interpreter.)

## `requirements.txt` — the recipe for your environment
A plain text file listing your project's packages (one per line, often pinned to a version). Anyone
(a teammate, a deploy server, your future self) runs `pip install -r requirements.txt` and gets the
**exact** same setup. This repo has one at the root — it grows as the AI track begins.

## Virtual environments (one sentence now, more in Phase 1)
A **venv** is an isolated package folder per project, so Project A's `requests==2.31` doesn't fight
Project B's `requests==2.20`. Create one with `python -m venv .venv` and activate it. We'll set this
up properly when the AI track starts; today just know *why* it exists.

## Importing safely (graceful degradation)
A third-party package might **not be installed**. Wrapping the import in `try/except ImportError`
(Module 02!) lets your program degrade gracefully instead of crashing — and tell the user how to fix
it. The demo file does exactly this with `requests`.

```python
try:
    import requests
except ImportError:
    requests = None
    print("requests not installed — run: pip install requests")
```

## 🎤 Talking points (what to say & focus on)
- **"PyPI is the reason Python won."** 500k packages, one command. This module is *why* the whole AI
  track is even possible on a free stack.
- **`python -m pip` over bare `pip`.** On machines with several Pythons, bare `pip` may install into
  the wrong one. `python -m pip` installs into *that exact* interpreter. Show the course's full path.
- **`requirements.txt` = reproducibility.** "Works on my machine" dies here. `pip freeze` →
  `requirements.txt` → anyone rebuilds your env. Tie it to deployment (every project this course ships
  needs one).
- **venv in one breath.** Don't teach activation today — just the *why* (isolation), so it's not scary
  in Phase 1. Promise the hands-on later.
- **The `try/except ImportError` demo is the payoff** — it reuses Module 02 and models real defensive
  code. Run it (the package isn't installed, so you'll see the graceful message), then explain how
  you'd install it. Errors + modules + pip, all in one runnable example.

## ⚠️ Common mistakes to call out
- `pip install` into the wrong Python (use `python -m pip`).
- Committing without a `requirements.txt` → nobody can reproduce your env.
- Confusing the **import name** with the **install name** (`pip install beautifulsoup4`, but
  `import bs4`; `pip install google-genai`, but `import google.generativeai`).
- Installing globally and hitting version conflicts (that's what venvs prevent).

Run the example (no internet needed — it handles the missing package gracefully):

```bash
python pip_demo.py
```

➡ Next: **[05-classes-and-objects](../05-classes-and-objects/)**
