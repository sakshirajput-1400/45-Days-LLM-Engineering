"""
Modules & imports — pull in Python's standard library instead of reinventing.

Run:
    python modules_and_imports.py
"""

# ----- The import styles -----
import math                       # whole module: use as math.<name>
from random import choice, randint  # pull specific names: use bare
import datetime as dt             # alias (shorter / convention)
import json                       # parse & produce JSON
import statistics                 # mean / median / stdev

# =====================================================================
# 1) math — constants and functions
# =====================================================================
print("math.pi        :", round(math.pi, 4))
print("math.sqrt(144) :", math.sqrt(144))
print("math.ceil(4.1) :", math.ceil(4.1))    # round UP
print()

# =====================================================================
# 2) random — the names we imported directly (no random. prefix)
# =====================================================================
import random
random.seed(7)                                # reproducible demo
print("randint(1, 6)  :", randint(1, 6))      # a dice roll
print("choice(menu)   :", choice(["tea", "coffee", "juice"]))
print()

# =====================================================================
# 3) datetime — real dates and time arithmetic
# =====================================================================
today = dt.date.today()
new_year = dt.date(today.year, 12, 31)
print("today          :", today)
print("days to Dec 31 :", (new_year - today).days)   # subtract dates -> timedelta
print()

# =====================================================================
# 4) json — the format every web API speaks (Phase 1 daily bread)
# =====================================================================
user = {"name": "Asha", "skills": ["python", "ai"], "active": True}
text = json.dumps(user)                        # Python dict -> JSON string
print("json.dumps     :", text)
back = json.loads(text)                         # JSON string -> Python dict
print("round-tripped  :", back["name"], back["skills"])
print()

# =====================================================================
# 5) statistics — don't hand-roll the maths
# =====================================================================
marks = [88, 72, 95, 60, 79]
print("mean           :", statistics.mean(marks))
print("median         :", statistics.median(marks))
print("stdev          :", round(statistics.pstdev(marks), 2))
print()

# =====================================================================
# 6) The __name__ guard — run-as-script vs import cleanly
# =====================================================================
def main():
    print("This runs because the file was executed directly.")

if __name__ == "__main__":     # True when run as `python modules_and_imports.py`
    main()                     # ...but NOT when another file imports this one
