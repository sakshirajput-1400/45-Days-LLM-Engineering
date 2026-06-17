"""
Inheritance & super() — reuse a base class, override what differs.

Run:
    python inheritance.py
"""

# =====================================================================
# 1) A base class and two children that OVERRIDE one method
# =====================================================================
class Animal:                          # parent / base
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."                   # generic default

class Dog(Animal):                     # Dog IS-A Animal
    def speak(self):                   # override
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Cat/Dog never define __init__ or `name` — they INHERIT it for free:
zoo = [Dog("Rex"), Cat("Luna"), Animal("Mystery")]
for creature in zoo:                   # each speaks its OWN way (polymorphism)
    print(f"{creature.name:<8} says {creature.speak()}")
print()

# =====================================================================
# 2) super() — extend the parent's setup instead of copy-pasting
# =====================================================================
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return f"{self.owner}: Rs {self.balance}"


class SavingsAccount(BankAccount):     # SavingsAccount IS-A BankAccount
    def __init__(self, owner, balance=0, rate=0.04):
        super().__init__(owner, balance)   # run parent's __init__ (sets owner/balance)
        self.rate = rate                   # then add our own field

    def add_interest(self):            # behaviour only savings accounts have
        self.balance += round(self.balance * self.rate, 2)
        return self.balance


acc = SavingsAccount("Asha", 10_000, rate=0.06)
print("start      :", acc)             # __str__ inherited from BankAccount
acc.add_interest()                     # method defined only on the child
print("with interest:", acc)
acc.withdraw(2000)                     # method inherited from the parent
print("after withdraw:", acc)
print()

# =====================================================================
# 3) Overriding AND extending: do the parent's work, then add more
# =====================================================================
class LoggedAccount(BankAccount):
    def withdraw(self, amount):
        print(f"  [log] {self.owner} is withdrawing Rs {amount}")
        result = super().withdraw(amount)   # reuse parent's logic (incl. the check)
        print(f"  [log] new balance Rs {result}")
        return result

ben = LoggedAccount("Ben", 500)
ben.withdraw(200)
# isinstance shows the "is-a" relationship Python tracks for us:
print("\nis ben a BankAccount?", isinstance(ben, BankAccount))   # True
print("is acc a SavingsAccount?", isinstance(acc, SavingsAccount))  # True
