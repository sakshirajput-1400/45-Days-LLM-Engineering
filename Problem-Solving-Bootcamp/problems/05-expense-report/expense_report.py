"""Problem 5 stub - expense report.

Run:  python expense_report.py

RULE 1: this problem is ABOUT decomposition. Name all your functions in the
STEP comments below BEFORE writing any of them. Then build and test them
ONE AT A TIME, starting with parse_line.
"""

SAMPLE = """2026-07-01,food,250
2026-07-02,travel,120

2026-07-03,food,90
oops this line is broken
2026-07-04,rent,8000
2026-07-05,food,310.50
2026-07-06,travel,4x0
"""


# STEP 1 (Understand): a "record" for one parsed line will be shaped like:
#                      ..............................................
#                      a line is BAD when: .................................
# STEP 2 (Example by hand): parse SAMPLE on paper.
#                      good records = ....  total = ....  biggest = ....
# STEP 3 (Plan): my functions, one job each, in build order:
#                      1) ........................  2) ........................
#                      3) ........................  4) ........................


def parse_line(line):
    """Turn one CSV line into a record, or None if the line is bad."""
    pass  # TODO: build and test THIS first (delete this line)


def load(text):
    """Parse every line of text; keep only the good records."""
    pass  # TODO (delete this line)


def category_totals(records):
    """Return a dict: category -> total amount spent on it."""
    pass  # TODO (delete this line)


def biggest(records):
    """Return the record with the largest amount (None if no records)."""
    pass  # TODO (delete this line)


# ---- STEP 5 (Test): run this file and compare with the expected report. ----
if __name__ == "__main__":
    records = load(SAMPLE) or []   # `or []` keeps this runnable while load is a TODO
    print(f"records parsed : {len(records)}   (expected 5)")

    total = sum(r["amount"] for r in records)
    print(f"total spent    : Rs. {total:.2f}   (expected Rs. 8770.50)")

    print(f"by category    : {category_totals(records)}")
    print("                 (expected food 650.5, travel 120, rent 8000)")

    top = biggest(records)
    print(f"biggest        : {top}")
    print("                 (expected the 2026-07-04 rent of 8000)")

    average = total / len(records) if records else 0
    print(f"average        : Rs. {average:.2f}   (expected Rs. 1754.10)")
