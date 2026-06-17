# 03 — Modules & Imports

A **module** is just a `.py` file full of reusable code. Python ships a huge **standard library**
("batteries included") — `math`, `random`, `datetime`, `json`, `os`, and dozens more — that you pull
in with `import`. Don't reinvent; import.

## The import styles
```python
import math                     # whole module -> use as math.sqrt(9)
math.sqrt(9)                    # 3.0

from math import sqrt, pi       # pull specific names -> use bare
sqrt(9)                         # 3.0

import datetime as dt           # alias (shorter / avoids clashes)
dt.date.today()

from math import *              # ❌ import everything — avoid (pollutes namespace)
```

| Style | Use when | Trade-off |
|-------|----------|-----------|
| `import module` | the default; clear where names come from | a bit more typing (`module.name`) |
| `from module import name` | you use a few names a lot | can clash with your own names |
| `import module as alias` | long names or a community convention (`np`, `pd`, `dt`) | reader must know the alias |
| `from module import *` | almost never | hides where names came from |

## A tour of useful standard-library modules
| Module | Gives you | Example |
|--------|-----------|---------|
| `math` | constants & functions | `math.sqrt`, `math.pi`, `math.ceil` |
| `random` | randomness (Day 3) | `random.randint`, `random.choice`, `random.shuffle` |
| `datetime` | dates & times | `datetime.date.today()`, time differences |
| `json` | parse/produce JSON | `json.dumps(obj)`, `json.loads(text)` |
| `os` / `pathlib` | files & paths | `Path("data").exists()` |
| `statistics` | mean/median/stdev | `statistics.mean([1,2,3])` |

`import` **runs the module once** (the first time) and caches it; later imports reuse it. The names
live in that module's **namespace** — which is exactly the **G**/**B** of Day-5's LEGB.

## Your own modules
Any `.py` you write is importable: `import helpers` then `helpers.greet()`. The
`if __name__ == "__main__":` guard lets a file *both* run as a script *and* be imported without its
demo code firing — you'll see it everywhere.

## 🎤 Talking points (what to say & focus on)
- **"Someone already wrote it — import it."** The standard library is free, tested, and vast. Frame
  importing as the professional default, not cheating.
- **`import math` vs `from math import sqrt`.** First keeps the source visible (`math.sqrt`); second
  is terser but can clash. Show both; recommend `import module` as the safe default for beginners.
- **Aliases are conventions, not magic** — `import numpy as np` is just a nickname. They'll meet
  `np`/`pd` constantly; demystify it now with `import datetime as dt`.
- **Avoid `from x import *`** — it dumps unknown names into your file and hides their origin. One
  sentence, firm.
- **`if __name__ == "__main__":` is the bridge** to real projects: a file that runs standalone *and*
  imports cleanly. The pip module and every library use it — plant it here.

## ⚠️ Common mistakes to call out
- Naming your file the same as a module you import (`random.py`) → it imports *itself*, weird errors.
- `from module import *` then not knowing where a name came from.
- Forgetting the `module.` prefix after `import module` (`sqrt(9)` → `NameError`).
- Re-implementing something the standard library already does (dates, json, stats).

Run the examples:

```bash
python modules_and_imports.py
```

➡ Next: **[04-pip-and-third-party](../04-pip-and-third-party/)**
