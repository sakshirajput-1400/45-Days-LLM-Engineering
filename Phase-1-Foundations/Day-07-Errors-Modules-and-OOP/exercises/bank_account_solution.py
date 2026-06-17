"""
Exercise 2 — Bank Account (solution).

Run:
    python bank_account_solution.py
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = []                 # a running log of operations

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount
        self.transactions.append(("deposit", amount))
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self.balance:
            raise ValueError(f"insufficient funds (have Rs {self.balance})")
        self.balance -= amount
        self.transactions.append(("withdraw", amount))
        return self.balance

    def statement(self):
        print(f"--- Statement for {self.owner} ---")
        for kind, amount in self.transactions:
            sign = "+" if kind == "deposit" else "-"
            print(f"  {kind:<9} {sign} Rs {amount}")
        print(f"  Balance     = Rs {self.balance}")

    def __str__(self):
        return f"{self.owner}: Rs {self.balance} ({len(self.transactions)} txns)"


# --- Drive it ---
acc = BankAccount("Asha", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.deposit(1200)

# The object guards itself — an overdraft is refused:
try:
    acc.withdraw(50_000)
except ValueError as e:
    print("Blocked:", e)

print(acc)            # __str__
acc.statement()
