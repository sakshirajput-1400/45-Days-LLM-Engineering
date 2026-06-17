# Day 07 — Exercises

Put today's tools to work: exceptions, `try/except`, modules, and OOP (classes + inheritance). Try
each in the stub file first, then check the matching `*_solution.py`.

---

## Exercise 1 — Safe Calculator 🧮
A calculator that never crashes on bad input — it catches the error and explains it.

**Your task:** in `safe_calculator.py`
1. `input()` two numbers and an operator (`+ - * /`).
2. Wrap the parsing in `try/except ValueError` so `"abc"` gives a friendly message, not a traceback.
3. Catch `ZeroDivisionError` for `/ 0`.
4. Bonus: `raise` a custom `UnknownOperatorError(Exception)` for an operator that isn't one of the four.

*Skills:* `try`/`except` (specific types), `raise`, a custom exception class, `float()`.
*Focus:* recovering from each failure mode with a clear message instead of crashing.

➡ Solution: [`safe_calculator_solution.py`](safe_calculator_solution.py)

---

## Exercise 2 — Bank Account 🏦
Model an account as a **class** — data plus the behaviour that protects it.

**Your task:** in `bank_account.py`
1. `class BankAccount:` with `__init__(self, owner, balance=0)`.
2. Methods: `deposit(amount)`, `withdraw(amount)` (refuse overdrafts — `raise ValueError`), `__str__`.
3. Track a `transactions` list (append each deposit/withdrawal) and add a `statement()` method.
4. Create an account, run a few operations, print the statement.

*Skills:* `class`, `__init__`, `self`, instance attributes/methods, `raise`, `__str__`, lists.
*Focus:* methods that guard state — the object refuses invalid operations.

➡ Solution: [`bank_account_solution.py`](bank_account_solution.py)

---

## Exercise 3 — Shapes & Inheritance 🔺
A base `Shape` with `Rectangle` and `Circle` subclasses — classic inheritance + `super()`.

**Your task:** in `shapes.py`
1. `class Shape:` with `__init__(self, name)` and an `area()` that returns `0` (a placeholder).
2. `class Rectangle(Shape):` — `__init__` takes width & height, calls `super().__init__("Rectangle")`,
   and **overrides** `area()`.
3. `class Circle(Shape):` — takes a radius, overrides `area()` (use `math.pi`).
4. Put several shapes in a list and loop, printing each `name` and `area()` (polymorphism!).

*Skills:* inheritance, `super().__init__`, overriding methods, `import math`, polymorphism.
*Focus:* `super()` to reuse the parent's setup; one loop, many shape behaviours.

➡ Solution: [`shapes_solution.py`](shapes_solution.py)

---

### Stretch goals (if you finish early)
- **Calculator:** loop it (Day 4) so it keeps calculating until the user types `quit`.
- **Bank:** add a `SavingsAccount(BankAccount)` with an `add_interest()` method (Module 07).
- **Shapes:** add a `Square(Rectangle)` that calls `super().__init__(side, side)`; add a `perimeter()`.
