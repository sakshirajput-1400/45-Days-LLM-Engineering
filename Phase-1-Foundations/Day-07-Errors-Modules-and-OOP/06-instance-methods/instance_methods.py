"""
Instance methods & attributes — bundle data WITH the behaviour that guards it.

Run:
    python instance_methods.py
"""

class BankAccount:
    # CLASS attribute: shared by every account (one copy on the class)
    bank_name = "SSAI Bank"

    def __init__(self, owner, balance=0):
        # INSTANCE attributes: unique to each account
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money; methods can VALIDATE (a raw dict can't)."""
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """Refuse to overdraw — the object protects its own state."""
        if amount > self.balance:
            raise ValueError(f"insufficient funds (have Rs {self.balance})")
        self.balance -= amount
        return self.balance

    def __str__(self):
        """What print(account) shows."""
        return f"[{self.bank_name}] {self.owner}: Rs {self.balance}"


# =====================================================================
# 1) Create accounts and call methods ON them
# =====================================================================
asha = BankAccount("Asha", 1000)
ben = BankAccount("Ben")               # balance uses the default 0

asha.deposit(500)                      # Python passes `asha` as self
asha.withdraw(200)
ben.deposit(50)

print(asha)                            # __str__ -> "[SSAI Bank] Asha: Rs 1300"
print(ben)
print()

# =====================================================================
# 2) The method GUARDS state — invalid operations raise (Module 02)
# =====================================================================
try:
    asha.withdraw(99999)
except ValueError as e:
    print("withdraw blocked:", e)
print()

# =====================================================================
# 3) Class attribute vs instance attribute
# =====================================================================
print("Shared bank name:", BankAccount.bank_name)
# Change it on the CLASS -> every instance sees the new value:
BankAccount.bank_name = "Softpro Bank"
print("asha now at      :", asha.bank_name)
print("ben now at       :", ben.bank_name)

# Setting self.x only affects THAT instance:
asha.bank_name = "Asha Private Bank"   # creates an instance attr that shadows the class one
print("asha overridden  :", asha.bank_name, "| ben still:", ben.bank_name)
