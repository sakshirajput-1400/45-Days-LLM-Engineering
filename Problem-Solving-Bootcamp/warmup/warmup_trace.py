"""Warm-up: trace before write.

READ THE RULES FIRST:
  1. Do NOT run this file yet.
  2. For each snippet below, trace it line by line ON PAPER and write down
     the exact output you expect.
  3. Only after predicting all 5, run:  python warmup_trace.py
  4. For every wrong prediction, re-trace until you can point at the exact
     line where your mental model differed from Python's.

Each snippet hides one classic trap. Getting one wrong is GOOD - it shows
you precisely where your mental model needs fixing.
"""

print("=" * 50)
print("SNIPPET 1 -- range boundaries")
print("=" * 50)
# Predict: what number prints?
total = 0
for n in range(1, 5):
    total += n
print(total)


print()
print("=" * 50)
print("SNIPPET 2 -- string slicing")
print("=" * 50)
# Predict: which characters print?
word = "python"
print(word[1:4])


print()
print("=" * 50)
print("SNIPPET 3 -- lists and order of operations")
print("=" * 50)
# Predict: what does the final list look like?
nums = [3, 8, 2]
nums.append(nums[0])
nums[0] = 9
print(nums)
#9382
#9828
#9823
#93823

print()
print("=" * 50)
print("SNIPPET 4 -- the sneaky else")
print("=" * 50)
# Predict: what count prints? (Trace EVERY character!)
count = 0
for ch in "banana":
    if ch == "a":
        count += 1
    else:
        count = 0
print(count)


print()
print("=" * 50)
print("SNIPPET 5 -- while + integer division")
print("=" * 50)
# Predict: what is x when the loop stops?
x = 10
while x > 3:
    x = x // 2
print(x)


print()
print("=" * 50)
print("Done. Score yourself: 5/5 = sharp simulator.")
print("Anything wrong? Re-trace it now - that's the rep.")
print("=" * 50)
