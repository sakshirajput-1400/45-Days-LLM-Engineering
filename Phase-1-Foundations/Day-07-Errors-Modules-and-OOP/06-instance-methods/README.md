# 06 — Instance Methods & Attributes

Attributes are an object's **data**; **methods** are its **behaviour** — functions that live inside a
class and act on `self`. This is the whole point of OOP: keep the data and the operations on it
together.

```python
class BankAccount:
    bank_name = "SSAI Bank"              # CLASS attribute — shared by all accounts

    def __init__(self, owner, balance=0):
        self.owner = owner               # INSTANCE attributes — unique per object
        self.balance = balance

    def deposit(self, amount):           # an instance METHOD (note self)
        self.balance += amount
        return self.balance

    def __str__(self):                   # how the object prints (a dunder)
        return f"{self.owner}'s account: Rs {self.balance}"

acc = BankAccount("Asha", 1000)
acc.deposit(500)                         # call a method ON the instance
print(acc)                               # uses __str__ -> "Asha's account: Rs 1500"
```

## Instance attribute vs class attribute
| | Instance attribute | Class attribute |
|--|--------------------|-----------------|
| Defined | in `__init__` via `self.x` | at class body level |
| Belongs to | one object | the class (shared by all) |
| Example | `self.balance` | `bank_name = "SSAI Bank"` |

Use a **class attribute** for things every instance shares (a bank name, a species, a default rate);
use **instance attributes** for per-object data.

## Methods always take `self` first
A method is just a function defined in a class whose first parameter is `self`. You call it as
`acc.deposit(500)` — Python passes `acc` as `self` automatically, so inside the method `self` *is*
`acc`.

## Useful dunder: `__str__`
`__str__` defines what `print(obj)` shows. Without it you get the ugly `<BankAccount object at
0x...>`. With it, your objects print like you mean them to.

## 🎤 Talking points (what to say & focus on)
- **Methods = verbs the object can do; attributes = nouns it has.** `account.deposit(500)` reads like
  a sentence. That readability is the OOP payoff — show the dict version (`account["balance"] +=
  500`) and how the method hides/guards that.
- **`self` again, in methods.** `acc.deposit(500)` → inside, `self` is `acc`, `amount` is 500. The
  caller never passes `self`. Reinforce from Module 05; it's still the #1 stumble.
- **Encapsulation = guarding state.** A `withdraw` method can *refuse* an overdraft (tie back to the
  Module 02 `raise`). A raw dict can't protect itself; a class method can. This is *why* classes.
- **Class vs instance attribute** with the `bank_name` demo: change it on the class, all instances
  see it; set `self.x`, only that object has it. Show both live — it surprises people.
- **`__str__` is the quick win** — make objects print nicely. Mention `__repr__`/other dunders exist
  (`__eq__`, `__len__`) without diving in; just enough to know the door is there.

## ⚠️ Common mistakes to call out
- Defining a method without `self` → `TypeError` when you call it.
- Accidentally sharing a *mutable* class attribute (e.g. a list) across all instances (same trap as
  Day-5 mutable defaults).
- Calling a method without `()` (`acc.deposit` vs `acc.deposit(500)`).
- Reading an attribute you never set in `__init__` → `AttributeError`.

Run the examples:

```bash
python instance_methods.py
```

➡ Next: **[07-inheritance-and-super](../07-inheritance-and-super/)**
