# 07 — Inheritance & `super()`

**Inheritance** lets a new class reuse and extend an existing one. The new class (**subclass / child**)
gets all the attributes and methods of the original (**base / parent**) for free, then adds or changes
what it needs. The test is **"is-a"**: a `SavingsAccount` *is a* `BankAccount`; a `Circle` *is a*
`Shape`.

```python
class Animal:                     # parent / base class
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):                # Dog inherits from Animal
    def speak(self):              # OVERRIDE the parent's method
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

Dog("Rex").speak()                # "Woof!"
Cat("Luna").name                  # "Luna" — inherited from Animal, no code repeated
```

## `super()` — reuse the parent instead of copy-pasting
When a child needs the parent's setup *plus* extra, call `super()`:
```python
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, rate=0.04):
        super().__init__(owner, balance)   # run the parent's __init__ first
        self.rate = rate                   # then add the child's own field

    def add_interest(self):                # behaviour only savings accounts have
        self.balance += self.balance * self.rate
        return self.balance
```
`super().__init__(...)` runs the parent's constructor so you don't re-type the owner/balance setup.
`super().method()` works for any method, not just `__init__`.

## Overriding
A child can **replace** a parent method by defining one with the same name (`speak` above). It can
also **extend** it — do the parent's work via `super().method()` then add more. This is how you
specialise behaviour without touching the parent.

## 🎤 Talking points (what to say & focus on)
- **"is-a" is the test for inheritance.** Dog is-a Animal ✅. A Car is *not* an Engine (it *has* one)
  → that's composition, not inheritance. Giving them the is-a litmus prevents the classic overuse.
- **Free reuse is the hook.** `Cat` never defines `__init__` or `name`, yet `Cat("Luna").name` works
  — inherited. Show how much code inheritance deletes.
- **Overriding = specialising.** Same method name, child's version wins. The `speak()` zoo demo (loop
  over a mixed list, each animal speaks its own way) is the memorable one — and it's polymorphism in
  disguise (one interface, many behaviours).
- **`super().__init__(...)` is the must-teach mechanic.** Without it, the child re-types the parent's
  setup (and drifts out of sync). With it, "do everything the parent does, then add mine." Walk the
  SavingsAccount example slowly.
- **AI tie-in:** frameworks lean on this hard — you'll subclass a base `Tool`, `Agent`, `Callback`, or
  `BaseModel` (Pydantic) and override one method. Today is the literal mechanic you'll use in Phase 3.

## ⚠️ Common mistakes to call out
- Forgetting `super().__init__(...)` → the parent's attributes never get set (`AttributeError` later).
- Using inheritance for "has-a" relationships (a `Car(Engine)` is wrong — a car *has* an engine).
- Deep inheritance chains (4+ levels) → hard to follow; prefer shallow + composition.
- Overriding a method but forgetting it needs the parent's work too (call `super()` to extend).

Run the examples:

```bash
python inheritance.py
```

➡ Next: **[08-lambda-functions](../08-lambda-functions/)** — tiny one-line functions for `sorted`/`map`/`filter`
