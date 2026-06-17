"""
Exercise 2 — Bank Account (STUDENT STUB).

Model an account as a class: data + the methods that protect it.
No input() — create an account and run operations directly.

Run:
    python bank_account.py
"""

# TODO: class BankAccount:
#   __init__(self, owner, balance=0):
#       self.owner, self.balance, self.transactions = [] (a log)
#   deposit(self, amount):
#       reject amount <= 0 (raise ValueError); add to balance; log it
#   withdraw(self, amount):
#       reject overdraft (raise ValueError); subtract; log it
#   statement(self):
#       print owner, every transaction, and the final balance
#   __str__(self):
#       return a one-line summary
#
# Then: make an account, deposit/withdraw a few times, print the statement.
