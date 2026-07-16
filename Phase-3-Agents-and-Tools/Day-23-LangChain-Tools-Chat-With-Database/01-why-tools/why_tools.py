"""
01 - Why tools? The one thing an LLM can't do on its own.

An LLM predicts text. It cannot reliably do arithmetic and it cannot see data
that wasn't in its training set (like YOUR database). A "tool" is just a normal
Python function we let the model ask us to run.

This script needs NO API key and NO model. It SIMULATES what a real model does:
when it can't answer directly, it emits a small structured request -- "call this
function with these arguments" -- and OUR code runs the function. That model ->
tool -> model hand-off is the entire idea behind tools and agents.

Run:
    python why_tools.py
"""

import json

# ----------------------------------------------------------------------------
# 1. The problem: text prediction is bad at exact facts.
# ----------------------------------------------------------------------------
# Imagine asking a model "what is 48973 * 215?". It will produce a number that
# LOOKS right but often isn't, because it's predicting digits, not calculating.
print("=" * 60)
print("The problem")
print("=" * 60)
question = "What is 48973 * 215?"
correct = 48973 * 215
a_typical_llm_guess = 10_500_000  # plausible-looking, but WRONG
print(f"Question: {question}")
print(f"  A text-only model might guess: {a_typical_llm_guess}")
print(f"  The real answer is:            {correct}")
print("  -> Guessing digits is not the same as calculating.\n")

# ----------------------------------------------------------------------------
# 2. The fix: give the model a tool (a plain Python function).
# ----------------------------------------------------------------------------
# These are ordinary functions. Nothing magic yet -- the model can't run them.
def calculator(a: float, b: float) -> float:
    """Multiply two numbers exactly."""
    return a * b

def order_count(city: str) -> int:
    """Pretend database lookup: orders shipped to a city (data the model never saw)."""
    fake_db = {"Pune": 27, "Mumbai": 41, "Delhi": 33}
    return fake_db.get(city, 0)

# A registry: name -> the actual function. Our code uses this to dispatch.
TOOLS = {"calculator": calculator, "order_count": order_count}

# ----------------------------------------------------------------------------
# 3. What the model actually sends back.
# ----------------------------------------------------------------------------
# A real model, given tools, does NOT return prose. It returns a structured
# "tool call": the name of the function plus the arguments. We hard-code two
# here to stand in for the model's decision.
model_tool_calls = [
    {"name": "calculator", "args": {"a": 48973, "b": 215}},
    {"name": "order_count", "args": {"city": "Pune"}},
]

print("=" * 60)
print("The fix: model asks, our code runs")
print("=" * 60)
for call in model_tool_calls:
    # The "model" asked for this -- print it so you can see the request.
    print(f"Model wants: {call['name']}({json.dumps(call['args'])})")

    # OUR code does the actual work -- look up the function and run it.
    func = TOOLS[call["name"]]
    result = func(**call["args"])

    # We'd hand this result back to the model, which then writes the final reply.
    print(f"  our code ran it -> {result}")
    print(f"  model can now answer using the REAL value: {result}\n")

# ----------------------------------------------------------------------------
# 4. The takeaway.
# ----------------------------------------------------------------------------
print("=" * 60)
print("Takeaway")
print("=" * 60)
print("The model supplies the THINKING (which tool, what arguments).")
print("Your code supplies the DOING (actually running the function).")
print("That model -> tool -> model hand-off is what the next modules make real")
print("with @tool and a live Groq model.")
