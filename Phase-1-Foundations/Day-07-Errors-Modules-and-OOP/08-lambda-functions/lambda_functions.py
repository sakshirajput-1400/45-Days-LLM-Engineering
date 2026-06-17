"""
Lambda functions — tiny, throwaway functions you write inline (no def, no name).

A lambda is just a shorter way to write a small function. These two are identical:
    def add(a, b): return a + b
    add = lambda a, b: a + b
Lambdas shine when a function wants *another function* as an argument
(sorted, max, map, filter) and writing a full `def` would be overkill.

Run:
    python lambda_functions.py
"""

# =====================================================================
# 1) def vs lambda — the same function, two ways to write it
# =====================================================================
def square_def(n):            # the familiar way
    return n * n

square_lambda = lambda n: n * n   # same thing, as an expression

print("square_def(5)    :", square_def(5))      # 25
print("square_lambda(5) :", square_lambda(5))   # 25
# Note: `lambda` has no `return` — the expression after the colon IS the result.
print()

# =====================================================================
# 2) Many args, no args — the syntax bends like a normal function
# =====================================================================
add = lambda a, b: a + b
full_name = lambda first, last: first + " " + last
greet = lambda: "Hello!"      # zero arguments

print("add(3, 4)        :", add(3, 4))                  # 7
print("full_name(...)   :", full_name("Asha", "Rao"))   # Asha Rao
print("greet()          :", greet())                    # Hello!
print()

# =====================================================================
# 3) The real use: passing a function to sorted() via key=
# =====================================================================
# Sort a list of (name, marks) tuples by the marks (index 1), high to low.
students = [("Asha", 88), ("Ravi", 72), ("Meena", 95), ("Karan", 60)]

by_marks = sorted(students, key=lambda pair: pair[1], reverse=True)
print("top scorer       :", by_marks[0])     # ('Meena', 95)
print("ranked           :", by_marks)
# Without lambda you'd write a whole named function just to pull out pair[1].

# Sort words by length, then alphabetically — key can return a tuple.
words = ["banana", "fig", "apple", "kiwi"]
print("by length        :", sorted(words, key=lambda w: (len(w), w)))
print()

# =====================================================================
# 4) max / min with key= — "biggest by what measure?"
# =====================================================================
prices = {"tea": 20, "coffee": 45, "juice": 35}
costliest = max(prices, key=lambda item: prices[item])
print("costliest drink  :", costliest)        # coffee
print()

# =====================================================================
# 5) map() and filter() — transform / keep, one item at a time
# =====================================================================
nums = [1, 2, 3, 4, 5, 6]

# map: apply a function to every item. Wrap in list() to see the result.
doubled = list(map(lambda n: n * 2, nums))
print("doubled          :", doubled)          # [2, 4, 6, 8, 10, 12]

# filter: keep only items where the function returns True.
evens = list(filter(lambda n: n % 2 == 0, nums))
print("evens            :", evens)            # [2, 4, 6]

# A list comprehension often reads better than map/filter — know both:
doubled_lc = [n * 2 for n in nums]
evens_lc = [n for n in nums if n % 2 == 0]
print("same, as comps   :", doubled_lc, evens_lc)
print()

# =====================================================================
# 6) When NOT to use a lambda
# =====================================================================
# If it needs a name, multiple lines, or any logic beyond one expression,
# use a normal def — it's clearer and shows up properly in tracebacks.
#
#   BAD : process = lambda x: ...long, reused-everywhere logic...
#   GOOD: def process(x): ...
#
# Rule of thumb: lambdas are for SHORT, ONE-OFF functions handed to another
# function (sorted/max/map/filter). Anything bigger -> def.

if __name__ == "__main__":
    print("Lambdas = small inline functions; reach for `def` once it grows.")
